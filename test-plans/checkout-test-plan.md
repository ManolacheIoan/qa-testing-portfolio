# Test Plan: Checkout Functionality

## Scope
In scope: Cart review before checkout, applying discount codes, shipping 
address entry, payment method selection, order confirmation.
Out of scope: Actual payment gateway integration testing (covered by 
payment provider's own certification), post-purchase email delivery.

## Test Objectives
- Confirm users can complete a purchase end-to-end with valid inputs
- Confirm discount codes apply correctly and reject invalid/expired codes
- Confirm the system handles edge cases (empty cart, out-of-stock items) gracefully
- Confirm order totals (subtotal, tax, shipping, discount) calculate correctly

## Test Approach
- Equivalence Partitioning & Boundary Value Analysis on quantity fields and 
  discount code inputs
- Cross-layer verification: confirm order data in the database matches what 
  the UI displays after checkout (UI/API/DB cross-check)
- Manual functional testing for the full checkout flow
- Automated regression tests (Playwright) for the core happy path

## Test Environment
- Staging environment with test payment gateway (sandbox mode)
- Browsers: Chrome (latest), Safari (latest)
- Devices: Desktop and mobile viewport

## Entry Criteria
- Checkout feature deployed to staging with sandbox payment mode enabled
- Test discount codes available in staging database
- Acceptance Criteria confirmed with Product Owner

## Exit Criteria
- All planned test cases executed
- Zero open Critical/High severity bugs
- Order totals verified correct via direct database query, not just UI display

## Risks
- Sandbox payment gateway may behave differently than production gateway
- Discount code logic involves multiple business rules (stacking, expiry, 
  minimum order value) that may not all be documented upfront

## Test Scenarios (summary)
1. Complete checkout with valid cart, valid address, valid payment → success, 
   order confirmed
2. Apply valid discount code → total updates correctly
3. Apply expired/invalid discount code → error message, total unchanged
4. Attempt checkout with empty cart → checkout blocked with clear message
5. Attempt checkout with an item that went out of stock mid-session → 
   appropriate error, item flagged for removal
6. Order total (subtotal + tax + shipping − discount) matches value stored 
   in the database after order creation
7. Checkout with quantity at boundary values (0, 1, max allowed per item)

## Resources & Timeline
- Tester: 1 person, 3 days
- Automation: 3 new Playwright test cases added to existing CI/CD suite
