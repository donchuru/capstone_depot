# FILE: mock_data.py
from capstone_depot import db
from capstone_depot.models import User, Post

def add_mock_data():
    # Create test users
    users = [
        User(username='john_doe', email='john@example.com', password='password'),
        User(username='jane_doe', email='jane@example.com', password='password')
    ]

    for user in users:
        db.session.add(user)
    db.session.commit()

    # Create test posts
    posts = [
        {
            'title': 'AI-Powered Robot',
            'year': 2024,
            'team_members': 'John Doe, Jane Doe',
            'category': 'Computer Engineering',
            'content': 'An AI-powered robot that can navigate complex environments.',
            'user_id': users[0].id,
            'poster': '/static/images/david-capstone-project.jpg'
        },
        {
            'title': 'Solar Energy System',
            'year': 2023,
            'team_members': 'Jane Doe',
            'category': 'Electrical Engineering',
            'content': 'A novel solar energy system for residential buildings.',
            'user_id': users[1].id,
            'poster': '/static/images/david-capstone-project.jpg'
        },
        {
            'title': 'Remastered Pac-Man',
            'year': 2024,
            'team_members': 'Albert Dinh, Ashley Davis, Ali Muneer',
            'category': 'Software Engineering',
            'content': 'Pac-Man is a traditional arcade game that is widely known. Remastered Pac-Man is built upon this classic favourite with exciting new features to challenge you and your friends. Explore several new ways to play with different game modes, playable characters, and unique level maps!',
            'user_id': users[0].id,
            'poster': '/static/images/david-capstone-project.jpg'
        }
    ]

    for post_data in posts:
        post = Post(**post_data)
        db.session.add(post)
    db.session.commit()
