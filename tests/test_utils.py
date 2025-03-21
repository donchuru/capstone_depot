from capstone_depot.utils.username_generator import generate_username, generate_unique_username
from capstone_depot.models import User
from capstone_depot import db

def test_generate_username():
    """Test that generate_username returns a string with expected format."""
    username = generate_username()
    assert isinstance(username, str)
    assert '_' in username
    parts = username.split('_')
    assert len(parts) == 2

def test_generate_unique_username(app):
    """Test that generate_unique_username returns a unique username."""
    with app.app_context():
        # Create a user with a known username
        test_username = "adventurous_panda"
        user = User(
            username=test_username,
            email="test@example.com",
            password="test123"  # pragma: allowlist secret
        )
        db.session.add(user)
        db.session.commit()

        # Generate a new unique username
        new_username = generate_unique_username(User)
        assert new_username != test_username
        assert User.query.filter_by(username=new_username).first() is None
