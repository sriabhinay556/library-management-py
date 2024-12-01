from dearpygui.dearpygui import *
from database import add_book  # Import database function


def show_add_book_page(switch_to_home, username):
    """Render Add Book Page"""
    with window(tag="Add Book Page", width=500, height=400, no_resize=True):
        add_button(label="Back to Home", callback=lambda s, a: switch_to_home(username), width=150, height=40)
        add_spacing(count=2)
        add_text("Add a New Book", color=[255, 255, 255], indent=200)
        add_spacing(count=2)
        add_input_text(label="Book Title", tag="book_title", width=300)
        add_input_text(label="Author", tag="book_author", width=300)
        add_input_text(label="Publication Year", tag="book_year", width=300)
        add_spacing(count=2)
        add_button(label="Add Book", callback=handle_add_book, width=200, height=50)


def handle_add_book(sender, app_data):
    """Handle Add Book Logic"""
    title = get_value("book_title")
    author = get_value("book_author")
    year = get_value("book_year")
    if title and author and year:
        add_book(title, author, year)  # Add book to database
        add_text(f"Book '{title}' by {author} added successfully!", color=[0, 255, 0], parent="Add Book Page")
        set_value("book_title", "")
        set_value("book_author", "")
        set_value("book_year", "")
    else:
        add_text("Please fill in all fields.", color=[255, 0, 0], parent="Add Book Page")
