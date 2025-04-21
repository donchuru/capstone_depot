from flask import render_template, request, Blueprint
from capstone_depot.models import Post
from capstone_depot.posts.forms import CATEGORIES

categories = Blueprint('categories', __name__)

@categories.route("/category/<string:category>")
def category_posts(category):
    """
    Display posts from a specific category.

    Args:
        category: The category (Computer Engineering, Electrical Engineering)... to filter the posts against.
    """
    page = request.args.get('page', 1, type=int)
    category_posts = Post.query.filter_by(category=category).order_by(Post.year.desc()).paginate(page=page, per_page=10)
    return render_template('home.html',category=category, posts=category_posts, categories=CATEGORIES[1:])
