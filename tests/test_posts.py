import json
from flask import url_for

def test_create_post(client, test_user, app):
    # Login first
    response = client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    }, follow_redirects=True)
    assert b'Home' in response.data  # Verify login was successful

    # Create post
    response = client.post('/post/new', data={
        'title': 'Test Project',
        'year': '2024',
        'team_members': json.dumps([{'name': 'Test User', 'linkedin_url': 'https://linkedin.com/test'}]),
        'category': 'Software Engineering',
        'content': 'Test project description',
        'link': 'https://youtube.com/test'
    }, follow_redirects=True)
    assert response.status_code == 200  # Should be 200 with follow_redirects=True
    assert b'Your project has been created!' in response.data or b'Test Project' in response.data

def test_view_post(client, test_post, app):
    with app.app_context():
        response = client.get(f'/post/{test_post.id}')
        assert response.status_code == 200
        assert test_post.title.encode() in response.data
