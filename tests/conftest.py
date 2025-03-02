import pytest
from capstone_blog import create_app, db
from capstone_blog.models import User, Post
import json

@pytest.fixture
def app():
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

@pytest.fixture
def test_user(app):
    user = User(
        username='testuser',
        email='test@example.com',
        password='password'
    )
    with app.app_context():
        db.session.add(user)
        db.session.commit()
    return user

@pytest.fixture
def test_post(app, test_user):
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
    with app.app_context():
        db.session.add(post)
        db.session.commit()
    return post
