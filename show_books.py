from dearpygui.dearpygui import *
from database import list_all_books  # Import the function


def show_all_books_page(switch_to_home, username):
    """Render Show All Books Page"""
    with window(tag="Show Books Page", width=500, height=300, no_resize=True):
        add_button(label="Back to Home", callback=lambda s, a: switch_to_home(username), width=150, height=40)
        add_spacing(count=2)
        add_text("All Available Books", color=[255, 255, 255], indent=200)
        add_spacing(count=2)

        # Create a scrollable container for books
        with child_window(tag="books_list_container", width=450, height=180, border=True):
            books = list_all_books()  # Retrieve all books
            if books:
                for book in books:
                    add_text(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
            else:
                add_text("No books available.", color=[255, 0, 0])
