# Capstone Depot
Online repository for students to post their capstone projects and posters

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
