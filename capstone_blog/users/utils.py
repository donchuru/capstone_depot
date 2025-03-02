import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from capstone_blog import mail
import cloudinary


''' Saving user's uploaded image to our file system '''
def save_picture(form_picture):
    # Upload the image to Cloudinary
    uploaded_image = cloudinary.uploader.upload(form_picture)

    # Get the public URL of the uploaded image from Cloudinary
    picture_url = uploaded_image["secure_url"]

    # Perform resizing using Cloudinary's transformation features
    transformed_url = cloudinary.utils.cloudinary_url(
        picture_url,
        width=125,
        height=125,
        crop="thumb",
        radius="max",
        gravity="auto"
    )[0]

    return transformed_url

def send_reset_email(user):
     token = user.get_reset_token()
     msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
     msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
     mail.send(msg)
