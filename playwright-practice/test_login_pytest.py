import pytest
from playwright.sync_api import Page


class LoginPage:
    """Page Object pentru pagina de login."""

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("button[type='submit']")


class CheckboxesPage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/checkboxes")

    def check_first(self):
        self.page.locator("input[type='checkbox']").first.click()

def test_check_first_checkbox(page: Page):
    checkboxes_page = CheckboxesPage(page)
    checkboxes_page.goto()
    checkboxes_page.check_first()

    assert checkboxes_page.page.locator("input[type='checkbox']").first.is_checked()


class DropdownPage:

    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://the-internet.herokuapp.com/dropdown") 

    def select_option_1(self):
        self.page.select_option("#dropdown", "1") 


def test_select_dropdown_option(page: Page):
    dropdown_page = DropdownPage(page)
    dropdown_page.goto()
    dropdown_page.select_option_1()

    assert dropdown_page.page.locator("#dropdown").input_value() == "1"



class SecureAreaPage:
    """Page Object pentru pagina afișată după login reușit."""

    def __init__(self, page: Page):
        self.page = page

    def get_flash_message(self):
        return self.page.inner_text(".flash")


def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("tomsmith", "SuperSecretPassword!")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "secure" in message
    assert "invalid" not in message


def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wronguser", "wrongpassword")

    secure_page = SecureAreaPage(page)
    message = secure_page.get_flash_message()

    assert "invalid" in message
