import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"


class LoginPage:
    """Page Object for the saucedemo login page."""

    def __init__(self, page: Page):
        self.page = page
        self.error = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.page.fill("#user-name", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")


class InventoryPage:
    """Page Object for the products page shown after a successful login."""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")

    def sort_by(self, value):
        self.page.select_option("[data-test='product-sort-container']", value)

    def prices(self):
        texts = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]


def logged_in_inventory(page: Page) -> InventoryPage:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


def test_valid_login(page: Page):
    inventory = logged_in_inventory(page)

    expect(page).to_have_url(BASE_URL + "inventory.html")
    expect(inventory.title).to_have_text("Products")


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("standard_user", "", "Epic sadface: Password is required"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "unknown_user",
            "secret_sauce",
            "Epic sadface: Username and password do not match any user in this service",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
    ],
    ids=["empty_password", "empty_username", "wrong_password", "unknown_user", "locked_out_user"],
)
def test_invalid_login(page: Page, username, password, expected_message):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)

    expect(login_page.error).to_have_text(expected_message)
    expect(page).to_have_url(BASE_URL)


def test_add_product_to_cart(page: Page):
    inventory = logged_in_inventory(page)
    inventory.add_backpack_to_cart()

    expect(inventory.cart_badge).to_have_text("1")


def test_sort_price_low_to_high(page: Page):
    inventory = logged_in_inventory(page)
    inventory.sort_by("lohi")

    prices = inventory.prices()
    assert prices == sorted(prices)
