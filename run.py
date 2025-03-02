# will import from the __init__.py file
from capstone_depot import create_app, db
from capstone_depot.mock_data import add_mock_data
from flask import Flask

app = create_app('development')

# Remove the before_first_request decorator as it's deprecated in Flask 2.3+
# Instead, we'll use the with app.app_context() approach

@app.cli.command('init-db')
def init_db_command():
    """Clear existing data and create new tables."""
    db.drop_all()
    db.create_all()
    print('Initialized the database.')

@app.cli.command('seed-db')
def seed_db_command():
    """Seed the database with mock data."""
    add_mock_data()
    print('Added mock data to the database.')

if __name__ == '__main__':
    with app.app_context():
        # Create tables before running the app
        db.create_all()

        # Check if there's any data in the database
        from capstone_depot.models import User
        if User.query.first() is None:
            print("No users found. Adding mock data...")
            add_mock_data()
            print("Mock data added successfully!")

    app.run(debug=True)
