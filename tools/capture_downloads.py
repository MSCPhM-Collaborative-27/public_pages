"""Capture the VS Code and Git download pages for Setup 2.1."""
from playwright.sync_api import sync_playwright
import os

OUT = os.path.join(os.path.dirname(__file__), "captured")
os.makedirs(OUT, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)

    # 1. VS Code download page (shows Windows + Mac + Linux buttons)
    page.goto("https://code.visualstudio.com/download", wait_until="networkidle")
    for label in ("Reject", "Decline", "Reject all", "Accept"):
        try:
            page.get_by_role("button", name=label, exact=False).first.click(timeout=2000)
            break
        except Exception:
            pass
    page.wait_for_timeout(800)
    page.screenshot(path=os.path.join(OUT, "vscode-download-page.png"))

    # 2. Git for Windows download page
    page.goto("https://git-scm.com/download/win", wait_until="networkidle")
    page.wait_for_timeout(800)
    page.screenshot(path=os.path.join(OUT, "git-download-page.png"))

    browser.close()
print("done", os.listdir(OUT))
