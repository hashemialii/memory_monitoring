# Memory Monitoring API

This project is designed to monitor the RAM usage of a Windows system and expose the data through an API.

## Project Structure

- `app/`: Contains the main application logic.
  - `main.py`: The FastAPI application.
  - `database.py`: Database connection and setup.
  - `models.py`: Pydantic models.
  - `crud.py`: CRUD operations.
  - `schemas.py`: Request/Response schemas.
- `scripts/`: Contains the RAM monitoring script.
- `tests/`: Contains unit tests.
- `requirements.txt`: Python dependencies.
- `README.md`: Project documentation.

## How to Run

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
