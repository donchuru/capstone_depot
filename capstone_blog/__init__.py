from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from capstone_blog.config import config
import cloudinary

db = SQLAlchemy()
migrate = Migrate()

# to encrypt our passwords
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Configure cloudinary
    cloudinary.config( 
        cloud_name = app.config['CLOUDINARY_CLOUD_NAME'],
        api_key = app.config['CLOUDINARY_API_KEY'],
        api_secret = app.config['CLOUDINARY_API_SECRET']
    )

    from capstone_blog.users.routes import users
    from capstone_blog.posts.routes import posts
    from capstone_blog.main.routes import main
    from capstone_blog.errors.handlers import errors
    from capstone_blog.categories.routes import categories
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    app.register_blueprint(categories)

    return app