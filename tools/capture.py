"""Capture real screenshots of the org's public repo UI (logged out)."""
from playwright.sync_api import sync_playwright
import os

OUT = os.path.join(os.path.dirname(__file__), "captured")
os.makedirs(OUT, exist_ok=True)
REPO = "https://github.com/MSCPhM-Collaborative-27/public_pages"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page.goto(REPO, wait_until="networkidle")

    # dismiss cookie banner if present
    for label in ("Reject", "Decline", "Reject all"):
        try:
            page.get_by_role("button", name=label, exact=False).first.click(timeout=2000)
            break
        except Exception:
            pass
    page.wait_for_timeout(500)

    # 1. Code button popover with HTTPS clone URL
    page.get_by_role("button", name="Code").first.click()
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(OUT, "code-button-open.png"))
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)

    # 2. Branch selector dropdown open
    try:
        page.get_by_role("button", name="main branch").first.click(timeout=3000)
    except Exception:
        page.locator("button:has-text('main')").first.click()
    page.wait_for_timeout(1200)
    page.screenshot(path=os.path.join(OUT, "branch-dropdown-open.png"))

    browser.close()
print("done", os.listdir(OUT))
