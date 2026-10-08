import re
from playwright.sync_api import Page, expect

def test_login_with_locators(page: Page):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    # 3) verifică cu expect că URL-ul conține "inventory"
    expect(page).to_have_url(re.compile("inventory"))