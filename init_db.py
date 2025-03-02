from capstone_blog import create_app, db
from capstone_blog.mock_data import add_mock_data

app = create_app('development')

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()

    print("Creating all tables...")
    db.create_all()

    print("Adding mock data...")
    add_mock_data()

    print("Database initialized successfully!")
