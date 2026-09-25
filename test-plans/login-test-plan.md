# Test Plan: Login Functionality

## Scope
In scope: Login form validation, successful login, failed login handling, 
password reset link visibility.
Out of scope: Password reset flow itself, third-party SSO login (Google/Facebook).

## Test Objectives
- Confirm users can log in successfully with valid credentials
- Confirm the system rejects invalid credentials with a clear error message
- Confirm the login form validates input before submission

## Test Approach
- Equivalence Partitioning & Boundary Value Analysis on email/password fields
- Manual functional testing for UI behavior
- Automated regression tests (Playwright) for the happy path, run on every deploy

## Test Environment
- Staging environment (staging.example.com)
- Browsers: Chrome (latest), Safari (latest), Firefox (latest)
- Devices: Desktop only for this cycle

## Entry Criteria
- Login feature deployed to staging
- Acceptance Criteria confirmed with Product Owner

## Exit Criteria
- All planned test cases executed
- Zero open Critical/High severity bugs
- Automated regression suite passing in CI/CD

## Risks
- Limited time before release (2 days)
- Backend rate-limiting logic not fully documented — may need clarification mid-testing

## Test Scenarios (summary)
1. Login with valid email + valid password → success
2. Login with valid email + invalid password → error message, no access
3. Login with invalid email format → validation error before submission
4. Login with empty fields → validation error, submit button disabled
5. Multiple failed attempts → account temporarily locked (if applicable)
6. Login with valid credentials but inactive account → appropriate error message

## Resources & Timeline
- Tester: 1 person, 2 days
- Automation: existing Playwright suite extended with 2 new test cases
