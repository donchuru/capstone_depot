import os
from flask import Flask, redirect, url_for, flash, session, current_app
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import current_user, login_user
from sqlalchemy.orm.exc import NoResultFound
from capstone_depot import db
from capstone_depot.models import User
from capstone_depot.utils.username_generator import generate_unique_username
import json

# Create Google OAuth blueprint
def create_google_blueprint():
    blueprint = make_google_blueprint(
        client_id=os.environ.get("GOOGLE_CLIENT_ID"),
        client_secret=os.environ.get("GOOGLE_CLIENT_SECRET"),
        scope=["profile", "email"],
        storage=SQLAlchemyStorage(User, db.session, user=current_user, user_required=False),
    )

    # Setup OAuth authorized signal handler
    @oauth_authorized.connect_via(blueprint)
    def google_logged_in(blueprint, token):
        if not token:
            flash("Failed to log in with Google.", "danger")
            return False

        # Get Google user info
        resp = google.get("/oauth2/v1/userinfo")
        if not resp.ok:
            flash("Failed to fetch user info from Google.", "danger")
            return False

        google_info = resp.json()
        google_user_id = google_info["id"]

        # Find this OAuth token in the database or create it
        try:
            # Find existing user
            user = User.query.filter_by(oauth_provider="google", oauth_id=google_user_id).first()
            if user is None:
                # Try to find a user with the same email
                user = User.query.filter_by(email=google_info["email"]).first()

                if user is not None:
                    # Update existing user with OAuth info
                    user.oauth_provider = "google"
                    user.oauth_id = google_user_id
                    user.oauth_token = token["access_token"]
                    user.oauth_data = google_info
                    db.session.commit()
                else:
                    # Create a new user with a fun random username
                    username = generate_unique_username(User)

                    user = User(
                        username=username,
                        email=google_info["email"],
                        image_file=google_info.get("picture", "https://res.cloudinary.com/dxpmu1c0z/image/upload/v1689164141/default_tu17zb.png"),
                        password=None,
                        oauth_provider="google",
                        oauth_id=google_user_id,
                        oauth_token=token["access_token"],
                        oauth_data=google_info
                    )
                    db.session.add(user)
                    db.session.commit()
            else:
                # Update token for existing user
                user.oauth_token = token["access_token"]
                user.oauth_data = google_info
                db.session.commit()

            # Log in the user
            login_user(user)
            flash(f"Successfully signed in with Google as {user.username}.", "success")

            # Skip flask-dance handling
            return False

        except Exception as e:
            current_app.logger.error(f"Error during Google OAuth: {str(e)}")
            flash("An error occurred during sign in.", "danger")
            return False

    # Setup OAuth error signal handler
    @oauth_error.connect_via(blueprint)
    def google_error(blueprint, error, error_description=None, error_uri=None):
        msg = f"OAuth error from Google: {error}"
        if error_description:
            msg = f"{msg} - {error_description}"
        flash(msg, "danger")

    return blueprint
