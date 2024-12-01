from dearpygui.dearpygui import *
from database import add_user  # Import database function


def show_signup_page(switch_to_login):
    """Render Sign Up Page"""
    with window(tag="Sign Up Page"):
        add_text("Sign Up", color=[255, 255, 255])
        add_spacing(count=2)
        add_input_text(label="New Username", tag="signup_username", width=150)
        add_input_text(label="New Password", tag="signup_password", password=True, width=150)
        add_spacing(count=2)
        add_button(label="Register", callback=lambda s, a: handle_signup(s, a, switch_to_login))
        add_same_line()
        add_button(label="Back to Login", callback=lambda s, a: switch_to_login())


def handle_signup(sender, app_data, switch_to_login):
    """Handle Sign Up Logic"""
    username = get_value("signup_username")
    password = get_value("signup_password")
    if not username or not password:
        add_text("Fields cannot be empty.", color=[255, 0, 0], parent="Sign Up Page")
    elif add_user(username, password):  # Add user to database
        add_text("Sign Up successful! You can now log in.", color=[0, 255, 0], parent="Sign Up Page")
        switch_to_login()
    else:
        add_text("Username already exists.", color=[255, 0, 0], parent="Sign Up Page")
