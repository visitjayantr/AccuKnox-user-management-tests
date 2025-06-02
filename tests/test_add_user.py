# test_add_user.py
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.navigate_to_admin()
    admin.add_user("ESS", "Enabled", "JayantR ", "jayantr", "Jayant@12345")
    assert admin.is_user_present("Admin")
