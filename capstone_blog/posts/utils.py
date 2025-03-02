import os
import secrets
from PIL import Image
from flask import url_for, current_app
import cloudinary.uploader

''' Saving user's uploaded image to our file system '''
def save_poster(form_poster):
    # Upload the image to Cloudinary
    upload_result = cloudinary.uploader.upload(form_poster)

    # Get the public URL of the uploaded image from the upload result
    image_url = upload_result['secure_url']

    return image_url

''' Saving user's uploaded image to our file system '''
def update_poster(form_poster, current_poster):
     print(current_poster)
     # names may collide so use a random hex when saving them instead
     random_hex = secrets.token_hex(8)
     f_name, f_ext = os.path.splitext(form_poster.filename)
     picture_fn = random_hex + f_ext
     new_poster_path = os.path.join(current_app.root_path, 'static/posters', picture_fn)
     
     i = Image.open(form_poster)
     
     os.remove(os.path.join(current_app.root_path, "static/posters/", current_poster))

     i.save(new_poster_path)

     return picture_fn