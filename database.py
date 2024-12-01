import sqlite3

DB_NAME = "book_management.db"


def create_tables():
    """Create necessary tables for the application."""
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Users Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)

        # Books Table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL
        )
        """)

        conn.commit()


def add_user(username, password):
    """
    Add a new user to the database.

    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.

    Returns:
        bool: True if the user is added successfully, False otherwise.
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False  # Username already exists


def authenticate_user(username, password):
    """
    Check if the username and password are correct.

    Args:
        username (str): The username provided.
        password (str): The password provided.

    Returns:
        bool: True if the credentials are valid, False otherwise.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return cursor.fetchone() is not None


def add_book(title, author, year):
    """
    Add a book to the database.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
            conn.commit()
    except Exception as e:
        print(f"Error adding book: {e}")


def search_books(keyword):
    """
    Search books by title, author, or year.

    Args:
        keyword (str): The keyword to search for.

    Returns:
        list: A list of books matching the keyword.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query=""
        if keyword=="":
            query = "SELECT * FROM books"
        else:
            query = """
            SELECT * FROM books
            WHERE title LIKE ? OR author LIKE ? OR CAST(year AS TEXT) LIKE ?
            """
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()


def list_all_books():
    """
    Retrieve all books from the database.

    Returns:
        list: A list of all books.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()


def delete_all_books():
    """
    Delete all books from the database. (For testing or resetting the books table.)
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books")
        conn.commit()
