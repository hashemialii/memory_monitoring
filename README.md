# Memory Monitoring

This project is a system for monitoring system memory usage using Python and FastAPI. It continuously collects memory information, stores it in an SQLite database, and provides a simple API for accessing the stored data.

## Features

- Periodically collects system memory usage information
- Stores data in an SQLite database
- Provides an API for accessing memory usage data
- Cleans up and optimizes the database

## Prerequisites

- Python 3.7 or higher
- `pip` for managing Python packages

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/hashemialii/memory_monitoring.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd memory_monitoring
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the combined setup and monitoring script:**

    This script will start both the RAM monitoring script and the FastAPI server.

    ```bash
    python run_project.py
    ```

## Scripts

- `run_project.py`: Starts both the RAM monitoring script and the FastAPI server.
- `scripts/collect_ram_info.py`: Collects and inserts memory usage data into the database.
- `scripts/create_tables.py`: Sets up the database tables.

## Example API Endpoints

- `GET /`: Returns a welcome message.
- `GET /memory/?n=10`: Retrieves the last 10 memory usage records.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
