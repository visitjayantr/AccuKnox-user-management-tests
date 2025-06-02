from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_delete_user(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")

    admin_page = AdminPage(page)
    admin_page.navigate_to_admin()

    # Search for the user you want to delete
    username_to_delete = "jayntr"
    admin_page.search_user(jayantr)

    # Check if user exists before deleting
    assert admin_page.is_user_present(jayantr), "User not found before deletion."

    # Delete the user
    admin_page.delete_user(username_to_delete)

    # Search again to confirm deletion
    admin_page.search_user(username_to_delete)
    assert not admin_page.is_user_present(username_to_delete), "User still found after deletion."
