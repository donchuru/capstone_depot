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
