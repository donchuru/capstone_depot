import json

def test_create_post(client, test_user):
    # Login first
    client.post('/login', data={
        'email': 'test@example.com',
        'password': 'password'
    })

    # Create post
    response = client.post('/post/new', data={
        'title': 'Test Project',
        'year': '2024',
        'team_members': json.dumps([{'name': 'Test User', 'linkedin_url': 'https://linkedin.com/test'}]),
        'category': 'Software Engineering',
        'content': 'Test project description',
        'link': 'https://youtube.com/test'
    })
    assert response.status_code == 302  # Redirect after successful creation

def test_view_post(client, test_post):
    response = client.get(f'/post/{test_post.id}')
    assert response.status_code == 200
    assert test_post.title.encode() in response.data
