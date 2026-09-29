# Bug Report: Multiple tracking/analytics requests fail with HTTP 429 on altex.ro

**Title:** Analytics/tracking "collect" requests return 429 (Too Many Requests) on altex.ro homepage and checkout flow

**Environment:** Safari (latest), macOS, altex.ro (production), observed via Web Inspector Network + Console tabs

**Preconditions:** None — reproducible simply by browsing the site normally (homepage, donation widget, cart/checkout pages)

**Steps to Reproduce:**
1. Open altex.ro in Safari with Web Inspector open (Network + Console tabs)
2. Browse normally across a few pages (homepage, a donation widget, cart/checkout)
3. Observe the Network tab for requests named "collect"
4. Observe the Console tab for failed resource errors

**Expected Result:** Tracking/analytics requests should succeed (HTTP 200) or fail gracefully without flooding the console with errors

**Actual Result:** 
- Multiple "collect" requests return HTTP 429 with the response body:
```json
  {
    "error": "url_shed_rate_limit_exceeded",
    "error_description": "Your request has been denied. Please try again soon."
  }
```
- Console additionally shows:
  - `[Meta Pixel] - Duplicate Pixel ID: 850316188363350` (pixel initialized twice on the same page)
  - `[TikTok Pixel] - Missing 'content_id' parameter` (required for Video Shopping Ads attribution)
  - Several `WebKitBlobResource error 1` failures on blob: URLs

**Evidence:** Screenshot of Web Inspector Network tab (429 response) and Console tab (errors/warnings), captured via Cmd+Option+I

**Severity:** Low — does not block or visibly break the user-facing experience; the site remains fully usable
**Priority:** Depends on business context — likely Medium to High for the marketing/analytics team, since duplicate pixel firing and missing parameters mean ad platforms (Meta, TikTok) receive incomplete or duplicated conversion data, directly affecting paid ad attribution accuracy

## Notes
Found opportunistically while learning to use Safari's Web Inspector (Cmd+Option+I). A good example of a defect that is invisible to an end user but has real business impact (ad spend attribution), and of using Network + Console tabs together to diagnose it — the same troubleshooting approach covered in the Testing Life Cycle / Defect Troubleshooting notes.
