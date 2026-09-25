"""
Automated tests mapped to test-plans/login-test-plan.md

Covers:
- Scenario 1: Login with valid email + valid password -> success
- Scenario 2: Login with valid email + invalid password -> error message
- Scenario 3: Login with empty fields -> validation/error, no access
"""

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")


class SecureAreaPage:
    def __init__(self, page: Page):
        self.page = page

    def get_flash_message(self):
        return self.page.inner_text(".flash")


def test_scenario_1_valid_login_succeeds(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "secure" in message
    assert "invalid" not in message


def test_scenario_2_invalid_password_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("tomsmith", "wrongpassword")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "invalid" in message


def test_scenario_3_empty_fields_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "invalid" in message