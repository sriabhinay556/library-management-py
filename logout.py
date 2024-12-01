from dearpygui.dearpygui import *


def show_logout_page(switch_to_login):
    """Render Logout Page"""
    with window(tag="Logout Page"):
        add_button(label="Back to Login", callback=lambda s, a: switch_to_login())
        add_text("You have been logged out!", color=[255, 255, 255])
