import pytest
from capstone_blog import create_app, db, bcrypt
from capstone_blog.models import User, Post
import json
from unittest.mock import patch

@pytest.fixture
def app():
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        # Drop all tables after tests instead of trying to delete individual records
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def mock_cloudinary():
    """Mock the Cloudinary uploader to avoid actual uploads during tests"""
    with patch('cloudinary.uploader.upload') as mock_upload:
        mock_upload.return_value = {'secure_url': 'https://example.com/test_image.jpg'}
        yield mock_upload

@pytest.fixture
def test_user(app):
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
        user = User(
            username='testuser',
            email='test@example.com',
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        return user

@pytest.fixture
def test_post(app, test_user):
    with app.app_context():
        post = Post(
            title='Test Project',
            year=2024,
            team_members=json.dumps([
                {'name': 'Test User', 'linkedin_url': 'https://linkedin.com/test'}
            ]),
            category='Software Engineering',
            content='Test project description',
            link='https://youtube.com/test',
            poster='https://example.com/test.jpg',
            user_id=test_user.id
        )
        db.session.add(post)
        db.session.commit()
        return post
