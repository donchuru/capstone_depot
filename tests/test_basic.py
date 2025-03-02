def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Capstone Depot' in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About This Project' in response.data

def test_login_page(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Sign In' in response.data

def test_post_routes_exist(client):
    """Simple smoke test to verify post routes don't crash"""
    # Test post listing page (might 404 if no post with ID 1, but shouldn't crash)
    response = client.get('/post/1')
    assert response.status_code in [200, 404]  # Either found or not found is acceptable
    
    # Test new post page (should redirect to login if not authenticated)
    response = client.get('/post/new')
    assert response.status_code in [200, 302]  # Either OK or redirect is acceptable
