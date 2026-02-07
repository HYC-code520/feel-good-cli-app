import sqlite3
import os


def get_db_path():
    """Get the absolute path to the database file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "database", "mood_journal.db")


def initialize_database():
    """Create tables from schema.sql and seed data if tables are empty."""
    db_path = get_db_path()
    schema_path = os.path.join(os.path.dirname(db_path), "schema.sql")

    with sqlite3.connect(db_path) as con:
        with open(schema_path, "r") as f:
            con.executescript(f.read())

    from ..database.seed import seed_database
    seed_database(db_path)
