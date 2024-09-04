from app.database import create_tables


def setup_database():
    create_tables()
    print("Tables created successfully.")


if __name__ == "__main__":
    setup_database()
