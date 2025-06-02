from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_validate_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(page)
    admin_page.navigate_to_admin()

    username = "jayantr"

    # Search for the user
    admin_page.search_user(username)
    assert admin_page.is_user_present(username), f"User '{username}' not found for validation."

    # Validate role and status (example: "ESS", "Disabled")
    actual_role = admin_page.get_user_role(username)
    actual_status = admin_page.get_user_status(username)

    assert actual_role == "ESS", f"Expected role 'ESS' but got '{actual_role}'"
    assert actual_status == "Disabled", f"Expected status 'Disabled' but got '{actual_status}'"
