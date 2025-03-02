# Capstone Depot

A platform for showcasing university capstone projects.

## Features

- User authentication and profile management
- Project submission and management
- Category-based project organization
- Search and filtering capabilities
- Responsive design for mobile and desktop

## Technology Stack

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Cloud Storage**: Cloudinary
- **Deployment**: Heroku

## Local Development Setup

1. Clone the repository:

   ```
   git clone https://github.com/donchuru/capstone_depot.git
   cd capstone_depot
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file (see `.env.example` for required variables)

5. Initialize the database:

   ```
   flask db upgrade
   ```

6. Run the development server:
   ```
   flask run
   ```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment.

### CI Pipeline

The CI pipeline runs on every push and pull request to the main branch and performs:

- Code linting with flake8
- Unit tests with pytest
- Code coverage reporting

### CD Pipeline

The CD pipeline automatically deploys to Heroku when changes are pushed to the main branch, after all tests pass.

### Setting up GitHub Secrets

To enable the CI/CD pipeline, you need to set up the following secrets in your GitHub repository:

1. `HEROKU_API_KEY`: Your Heroku API key
2. `HEROKU_EMAIL`: The email associated with your Heroku account
3. `SECRET_KEY`: A secret key for your Flask application

## Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality and prevent sensitive data from being committed.

To set up pre-commit hooks:

```
pip install pre-commit
pre-commit install
```

## License

[MIT License](LICENSE)

## Files in root directory

- run.py
- requirements.txt
- Procfile
- README

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your values
6. Initialize the database: `flask init-db`
7. Seed the database with mock data: `flask seed-db`

## Development

Run the application locally:
