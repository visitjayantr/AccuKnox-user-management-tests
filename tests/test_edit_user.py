from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_edit_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(page)
    admin_page.navigate_to_admin()

    username_to_edit = "jayantr"

    # Search for the user
    admin_page.search_user(username_to_edit)
    assert admin_page.is_user_present(username_to_edit), "User not found for editing."

    # Edit the user details
    admin_page.edit_user(username_to_edit, new_status="Disabled")

    # Re-search to verify updates
    admin_page.search_user(username_to_edit)
    assert admin_page.get_user_status(username_to_edit) == "Disabled", "User status was not updated."
