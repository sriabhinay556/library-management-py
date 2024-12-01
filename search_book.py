from dearpygui.dearpygui import *
from database import search_books  # Import database function


def show_search_book_page(switch_to_home, username):
    """Render Search Book Page"""
    with window(tag="Search Book Page", width=450, height=380, no_resize=True):
        add_button(label="Back to Home", callback=lambda s, a: switch_to_home(username), width=150, height=40)
        add_spacing(count=2)
        add_text("Search for a Book", color=[255, 255, 255], indent=200)
        add_spacing(count=2)
        add_input_text(label="Search Keyword", tag="search_book_keyword", width=100)
        add_spacing(count=2)
        add_button(label="Search", callback=handle_search_book, width=200, height=50)
        add_spacing(count=2)
        
        # Create a scrollable container for search results
        with child_window(tag="search_results_container", width=300, height=200, border=True, horizontal_scrollbar=True):
            pass  # Initially empty, populated when search results are displayed


def handle_search_book(sender, app_data):
    """Handle Search Book Logic"""
    keyword = get_value("search_book_keyword")
    container = "search_results_container"

    # Clear previous search results
    delete_item(container, children_only=True)

    # Perform search
    results = search_books(keyword)

    # Display results
    if results:
        add_text("Search Results:", parent=container, color=[255, 255, 255])
        for book in results:
            add_text(f"- {book[1]} by {book[2]} ({book[3]})", parent=container)
    else:
        add_text("No results found.", parent=container, color=[255, 0, 0])

    # Clear the search input field
    set_value("search_book_keyword", "")
