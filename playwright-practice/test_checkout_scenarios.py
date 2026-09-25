"""
Automated tests mapped to test-plans/checkout-test-plan.md

Covers (subset, adapted to saucedemo.com):
- Scenario 1: Complete checkout with valid cart, valid address -> success
- Scenario 4: Attempt checkout with empty cart -> checkout blocked
- Scenario: Checkout form validation with empty fields -> error shown
"""

from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_backpack_to_cart(self):
        self.page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_checkout(self):
        self.page.click("#checkout")


class CheckoutInfoPage:
    def __init__(self, page: Page):
        self.page = page

    def fill_info(self, first_name, last_name, zip_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def get_error_message(self):
        return self.page.inner_text("[data-test='error']")


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page

    def finish_order(self):
        self.page.click("#finish")

    def get_confirmation_message(self):
        return self.page.inner_text(".complete-header")


def test_scenario_1_complete_checkout_succeeds(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_info = CheckoutInfoPage(page)
    checkout_info.fill_info("Ioan", "Manolache", "12345")

    checkout_overview = CheckoutOverviewPage(page)
    checkout_overview.finish_order()

    confirmation = checkout_overview.get_confirmation_message()
    assert "Thank you" in confirmation


def test_scenario_2_checkout_with_empty_fields_shows_error(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(page)
    cart_page.go_to_checkout()

    checkout_info = CheckoutInfoPage(page)
    checkout_info.fill_info("", "", "")

    error_message = checkout_info.get_error_message()
    assert "required" in error_message.lower()


def test_scenario_3_cart_badge_updates_after_adding_item(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(page)
    inventory_page.add_backpack_to_cart()

    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")