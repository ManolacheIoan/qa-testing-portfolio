# Exploratory Testing Session: saucedemo.com as `problem_user`

**Tester:** Ioan Manolache
**Charter:** Explore saucedemo.com logged in as `problem_user` to find visual or behavioral problems.
**Timebox:** 15 minutes
**Environment:** Chrome, macOS, https://www.saucedemo.com

## Confirmed bugs (each one has an automated test in `playwright-practice/test_problem_user_bugs.py`)

### BUG-1: "Remove" button on inventory page does not remove item from cart
- **Steps:** 1. Log in as `problem_user`. 2. Click "Add to cart" on the first product. 3. Click "Remove" on the same product.
- **Expected:** Item removed, cart badge disappears.
- **Actual:** Cart badge stays at 1.
- **Severity:** Medium (workaround: remove the item from the cart page).

### BUG-2: Sort dropdown does not reorder products
- **Steps:** 1. Log in as `problem_user`. 2. Select "Name (Z to A)" in the sort dropdown.
- **Expected:** Products reordered, first item is "Test.allTheThings() T-Shirt (Red)".
- **Actual:** Order unchanged, first item stays "Sauce Labs Backpack"; the selection does not persist in the dropdown.
- **Severity:** Medium.

### BUG-3: Only 3 of 6 products can be added to the cart
- **Steps:** 1. Log in as `problem_user`. 2. Click "Add to cart" on all 6 products.
- **Expected:** Cart badge shows 6.
- **Actual:** Cart badge shows 3.
- **Severity:** High (core purchase flow blocked for half of the catalog).

## Not reproduced
- **Cart pre-populated with 5 items on first login:** observed during the manual session, but not reproducible in a clean browser session (automated test passes). Most likely leftover state from earlier manual testing, so it was not reported as a bug.

## Lesson learned
Always reproduce in a clean environment before reporting. Automating the check separated real bugs from leftover browser state.
