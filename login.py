from dearpygui.dearpygui import *
from database import authenticate_user  # Import database function


def show_login_page(switch_to_home, switch_to_signup):
    """Render Login Page"""
    with window(tag="Login Page"):
        add_text("LIBRARY MANAGEMENT SYSTEM", color=[200, 100, 300])
        add_text("Login", color=[255, 255, 255])
        add_spacing(count=2)
        add_input_text(label="Username", tag="login_username", width=150)
        add_input_text(label="Password", tag="login_password", password=True, width=150)
        add_spacing(count=2)
        add_button(label="Login", callback=lambda s, a: handle_login(s, a, switch_to_home))
        add_same_line()
        add_button(label="Sign Up", callback=lambda s, a: switch_to_signup())


def handle_login(sender, app_data, switch_to_home):
    """Handle Login Logic"""
    username = get_value("login_username")
    password = get_value("login_password")
    if authenticate_user(username, password):  # Use database to verify credentials
        delete_item("Login Page")
        switch_to_home(username)
    else:
        add_text("Invalid username or password.", color=[255, 0, 0], parent="Login Page")
