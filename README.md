# Capstone Depot
Online repository for uAlberta students to post their capstone projects and posters.

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
   python init_db.py
   ```

6. Run the development server:
   ```
   python run.py
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

## Pre-commit Hooks
This project uses pre-commit hooks to ensure code quality and prevent sensitive data from being committed.
To set up pre-commit hooks:

```
pip install pre-commit
pre-commit install
```

## Contributing Guide
We welcome contributions to Capstone Depot! This guide will help you get started as a contributor.

### Getting Started
1. **Fork the Repository**: Start by forking the repository to your GitHub account.

2. **Clone Your Fork**:
   ```
   git clone https://github.com/YOUR-USERNAME/capstone_depot.git
   cd capstone_depot
   ```

3. **Set Up Development Environment**: Follow the **"Local Development Setup"** section above.

4. **Create a Branch**:
   ```
   git checkout -b feature/your-feature-name
   ```

### Development Workflow
1. **Make Your Changes**: Implement your feature or bug fix.

2. **Commit Your Changes**: Use clear, descriptive commit messages.
   ```
   git commit -m "Add feature: brief description of what you did"
   ```

3. **Push to Your Fork**:
   ```
   git push origin feature/your-feature-name
   ```

4. **Submit a Pull Request**: Go to the original repository and create a pull request from your branch.

### Pull Request Guidelines
1. **Description**: Provide a detailed description of your changes.
2. **Issue Reference**: Link to any related issues.
3. **Tests**: Ensure all tests pass.
4. **Documentation**: Update documentation if necessary.
5. **Code Style**: Follow the project's coding standards.

### Code Review Process
1. At least one maintainer will review your PR
2. Address any requested changes
3. Once approved, a maintainer will merge your PR

### Project Structure
- `capstone_depot/` - Main application package
  - `models/` - Database models
  - `routes/` - Route definitions
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
- `tests/` - Test suite
- `migrations/` - Database migrations

### Reporting Bugs
If you find a bug, please report it by creating an issue in the GitHub repository.

Please make sure to include the following:
1. A clear, descriptive title
2. Steps to reproduce the bug
3. Expected behavior
4. Actual behavior
5. Screenshots if applicable
6. Your environment (OS, browser, etc.)

## License
[MIT License](LICENSE)
