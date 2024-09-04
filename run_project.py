import subprocess
import os
import time


def run_in_new_terminal(command, cwd=None):
    """Runs a command in a new terminal window."""
    # Use `start` to open a new Command Prompt on Windows
    subprocess.Popen(f'start cmd /k "{command}"', cwd=cwd, shell=True)


def check_and_create_database(db_path, create_script):
    """Checks if the database exists, and creates it if it doesn't."""
    if not os.path.exists(db_path):
        print("Database not found. Creating database...")
        subprocess.run(['python', '-m', create_script], check=True)
        print("Database created successfully.")
    else:
        print("Database already exists.")


def main():
    project_dir = r"C:\Users\aliha\PycharmProjects\memory_test"
    db_path = os.path.join(project_dir, "memory_info.db")
    create_script = 'scripts.create_tables'

    # Change the current working directory
    os.chdir(project_dir)

    # Check and create the database if it doesn't exist
    check_and_create_database(db_path, create_script)

    # Define the commands
    command1 = 'python -m scripts.collect_ram_info'
    command2 = 'uvicorn app.main:app --reload'

    # Run the commands in separate terminals
    run_in_new_terminal(command1)
    time.sleep(2)  # Sleep to ensure the first terminal starts properly
    run_in_new_terminal(command2)


if __name__ == "__main__":
    main()
