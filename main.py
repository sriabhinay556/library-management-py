from dearpygui.dearpygui import *
from login import show_login_page
from signup import show_signup_page
from add_book import show_add_book_page
from search_book import show_search_book_page
from show_books import show_all_books_page


def show_home_page(username):
    """Render Home Page"""
    with window(tag="Home Page", width=500, height=300, no_resize=True):
        add_text(f"Welcome, {username}!", color=[0, 255, 0], indent=200)
        add_spacing(count=3)
        add_button(label="Add Book", callback=lambda s, a: switch_to_add_book(username), width=200, height=50)
        add_button(label="Search Book", callback=lambda s, a: switch_to_search_book(username), width=200, height=50)
        add_button(label="Show All Books", callback=lambda s, a: switch_to_show_books(username), width=200, height=50)
        add_button(label="Logout", callback=switch_to_login, width=200, height=50)


def switch_to_add_book(username):
    hide_all_pages()
    show_add_book_page(switch_to_home, username)


def switch_to_search_book(username):
    hide_all_pages()
    show_search_book_page(switch_to_home, username)


def switch_to_show_books(username):
    hide_all_pages()
    show_all_books_page(switch_to_home, username)


def switch_to_login():
    hide_all_pages()
    show_login_page(show_home_page, switch_to_signup)


def switch_to_signup():
    hide_all_pages()
    show_signup_page(switch_to_login)


def switch_to_home(username):
    hide_all_pages()
    show_home_page(username)


def hide_all_pages():
    """Hide all pages to keep only one visible"""
    for page in ["Home Page", "Add Book Page", "Search Book Page", "Sign Up Page", "Login Page", "Show Books Page"]:
        if does_item_exist(page):
            delete_item(page)


if __name__ == "__main__":
    create_context()
    create_viewport(title="Dear PyGui Book Management System", width=600, height=400)
    show_login_page(show_home_page, switch_to_signup)  # Start with the Login Page
    setup_dearpygui()
    show_viewport()
    start_dearpygui()
    destroy_context()
