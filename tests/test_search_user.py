from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(page)
    admin_page.navigate_to_admin()

    username_to_search = "jayantr"

    # Perform the search
    admin_page.search_user(username_to_search)

    # Verify user is found in the result
    assert admin_page.is_user_present(username_to_search), f"User '{username_to_search}' not found in search results."
