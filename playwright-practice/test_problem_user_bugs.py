"""
Automated checks for issues found during the exploratory testing session
on saucedemo.com as `problem_user`.

Tests marked xfail document CONFIRMED bugs: they assert the expected
behavior, and currently fail because the application misbehaves.
"""

import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture
def problem_page(page: Page):
    page.goto(BASE_URL)
    page.fill("#user-name", "problem_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    return page


def test_cart_is_empty_after_fresh_login(problem_page: Page):
    # Not reproducible in a clean browser: the 5 pre-populated items seen
    # manually were leftover state from an earlier session.
    expect(problem_page.locator(".shopping_cart_badge")).to_have_count(0)


@pytest.mark.xfail(strict=True, reason="BUG: only 3 of 6 products can be added to the cart")
def test_all_products_can_be_added_to_cart(problem_page: Page):
    buttons = problem_page.locator("button.btn_inventory")
    expect(buttons).to_have_count(6)

    for i in range(6):
        buttons.nth(i).click()

    expect(problem_page.locator(".shopping_cart_badge")).to_have_text("6")


@pytest.mark.xfail(strict=True, reason="BUG: Remove button on inventory page does not remove the item")
def test_remove_button_on_inventory_removes_item(problem_page: Page):
    button = problem_page.locator("button.btn_inventory").first
    button.click()  # add
    button.click()  # remove

    expect(problem_page.locator(".shopping_cart_badge")).to_have_count(0)


@pytest.mark.xfail(strict=True, reason="BUG: sort dropdown does not reorder the products")
def test_sort_za_reorders_products(problem_page: Page):
    problem_page.select_option(".product_sort_container", "za")

    first_item = problem_page.locator(".inventory_item_name").first
    expect(first_item).to_have_text("Test.allTheThings() T-Shirt (Red)")
