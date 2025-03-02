"""
This file contains all the routes that are related to posts on Capstone Depot (https://www.capstonedepot.live/).

Functionality supported around posts inculdes:
    making a new post
    viewing a post's details
    updating a post
    deleting a post

Author: David Onchuru
"""

from flask import render_template, url_for, flash, redirect, request, abort ,Blueprint
from flask_login import current_user, login_required
from capstone_blog import db  # Project database
from capstone_blog.models import Post  # Database table
from capstone_blog.posts.forms import PostForm  # Web form to put in Post details

# save_poster() is a utility method to check poster format and save it to a cloud storage service (currently Cloudinary).
# It returns a url with the link to the resource and also performs error checking
from capstone_blog.posts.utils import save_poster

posts = Blueprint('posts', __name__)


@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
     """
     Route to make a new post.

     This route initializes a form to take in the project's details
     The form details are then entered into the Post table in the database.
     """
     form = PostForm()
     # validate_on_submit() will validate the format of the form and make sure the user fills in the right fields before saving their changes to the database
     if form.validate_on_submit():
          # Preprocessing to get poster url in database table
          if form.poster.data:  # Check if a file was uploaded for the poster field
               poster_url = save_poster(form.poster.data)  # Assign the saved file path to poster_file
               print(poster_url)

          post = Post(
               title=form.title.data,
               year = form.year.data,
               team_members = form.team_members.data,
               content=form.content.data,
               category=form.category.data,
               link=form.link.data,
               poster=poster_url,  # Assign the value of poster_file to the poster column
               author=current_user
          )

          print("***** BEFORE WE COMMIT TO DB ********") # useful for debugging
          db.session.add(post)
          db.session.commit()
          flash(f'Your project has been created!', 'success')
          return redirect(url_for('main.home'))

     return render_template('create_post.html', title='Upload a Project', form=form, legend='Upload a Project')


@posts.route("/post/<int:post_id>")
def post(post_id):
     """
     Route to view a project's details.

     All the project details are queried from the database using the post's id and rendered from the post HTML template.
     """
     post = Post.query.get_or_404(post_id)
     return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
     """
     Route to update a project's details.

     All the project details are queried from the database and prepopulated.
     After changes have been made, the post is updated and rendered dynamically with the Post HTML template.
     """
     post = Post.query.get_or_404(post_id)
     if post.author != current_user:
          abort(403)

     form = PostForm()

     if form.validate_on_submit():
          # Update the contents of the post in our db
          post.title = form.title.data
          post.year = form.year.data
          post.team_members = form.team_members.data
          post.content = form.content.data
          post.category = form.category.data

          # Patch for link bug. Check issue #37
          if form.link.data:
               post.link = form.link.data
          else:
               post.link = ""

          if form.poster.data:
               poster_url = save_poster(form.poster.data)
               post.poster = poster_url
          db.session.commit()
          flash('Your project has been updated!', 'success')
          return redirect(url_for('posts.post', post_id=post.id)) # Show user the updated post

     # After user has pressed the update post button
     # All form fields get pre-populated by querying the post's details from the database
     elif request.method == 'GET':
          form.title.data = post.title
          form.year.data = post.year
          form.team_members.data = post.team_members
          form.content.data = post.content
          form.category.data = post.category
          form.link.data = post.link
          form.poster.data = post.poster
     return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
     """
     Route to delete a post.

     Deletes the posts entry from the Posts table in the database.
     After delete action, user is redirected to home page.
     """
     post = Post.query.get_or_404(post_id)
     if post.author != current_user:
          abort(403)
     db.session.delete(post)
     db.session.commit()
     flash('Your project has been deleted!', 'success')
     return redirect(url_for('main.home'))
