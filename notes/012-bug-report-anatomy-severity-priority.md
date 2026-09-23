# Bug Report Anatomy & Severity vs Priority

## Why it matters
A poorly written bug report means the developer can't reproduce the issue, leading to back-and-forth and wasted time. A good bug report lets the developer understand the problem on the first read.

## The 7 components of a complete bug report

1. **Title** — [Component/Page] + [What's wrong] + [Condition, if relevant]
   - Bad: "Login doesn't work"
   - Good: "Login button unresponsive on Safari after 3 failed login attempts"

2. **Environment** — browser + version, OS, device, app/build version being tested

3. **Preconditions** — what must be true before starting the steps (e.g. "User logged in with a non-admin account")

4. **Steps to Reproduce** — numbered, exact, unambiguous, one action per step

5. **Expected Result** — what should happen, based on requirements/Acceptance Criteria

6. **Actual Result** — what actually happens (exact error messages, not paraphrased)

7. **Evidence** — screenshot, video, or console/network/server logs

## Example

Title: Checkout page crashes when applying two discount codes simultaneously

Environment: Chrome 128, Windows 11, staging build v2.4.1

Preconditions: User logged in, cart contains 1 item, valid discount code "SAVE10" available

Steps to Reproduce:
1. Add item to cart, go to checkout
2. Apply discount code "SAVE10"
3. In the same field, apply a second code "WELCOME5" without refreshing
4. Click "Apply"

Expected Result: System should either reject the second code with a clear message or stack them per business rules

Actual Result: Page throws a 500 error and checkout becomes unresponsive; console shows `TypeError: Cannot read property 'discountValue' of undefined`

## Severity vs Priority

**Severity** — how technically broken the bug is (objective, independent of business context)
**Priority** — how urgently it needs to be fixed (a business/planning decision)

These are independent and often confused.

### Severity levels
- Critical — system crashes, data lost/corrupted, core functionality blocked
- High — major functionality affected, but a workaround exists
- Medium — minor functionality affected, limited impact
- Low — cosmetic/UI issues, no functional impact

### Priority levels
- P1/Urgent — fix immediately, blocks release or affects many users now
- P2/High — fix in current sprint
- P3/Medium — can wait for next sprint
- P4/Low — nice to have, fixed when time allows

### The 4 combinations (common interview question)
- **High Severity, High Priority**: A crash on the homepage right before launch
- **High Severity, Low Priority**: A crash in a rarely-used feature from a legacy module about to be deprecated
- **Low Severity, High Priority**: A typo on the checkout page right before a major press event
- **Low Severity, Low Priority**: Wrong color on a secondary button on a rarely visited page

## Who sets what
- QA/Tester — typically sets Severity, based on technical impact
- Product Owner/Team Lead/PM — typically sets Priority, based on business context
