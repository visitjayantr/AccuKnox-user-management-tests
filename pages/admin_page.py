# pages/admin_page.py

from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_menu = page.locator("a:has-text('Admin')")
        self.add_button = page.locator("button:has-text('Add')")
        # Add other selectors here...

    def navigate_to_admin(self):
        self.admin_menu.click()

    def add_user(self, role, status, emp_name, username, password):
        self.add_button.click()
        # Fill the form here...
