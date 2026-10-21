#!/usr/bin/env python3
"""
Screenshot generator using Playwright.
Captures desktop and mobile screenshots of all pages.

Requirements: playwright, chromium
Install: pip install playwright && playwright install chromium
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import os

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = REPO_ROOT / "screens"
BASE_URL = os.environ.get('AGRIMASTER_URL', 'http://localhost:8080')

# Screenshot jobs: (page, name, width)
JOBS = [
    ("index", "desktop", 1440),
    ("index", "mobile", 390),
    ("about", "about", 1440),
    ("products", "products", 1440),
    ("contact", "contact", 1440),
    ("index", "mobile-menu", 390)
]

def main():
    """Generate screenshots"""
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/usr/bin/google-chrome",
            args=["--no-sandbox"]
        )
        
        for page_name, screenshot_name, width in JOBS:
            print(f"Capturing {screenshot_name}...")
            
            height = 900 if width > 400 else 844
            page = browser.new_page(viewport={"width": width, "height": height})
            
            # Navigate and wait for images
            page.goto(f"{BASE_URL}/{page_name}.html", wait_until="networkidle")
            page.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
            page.wait_for_timeout(800)
            
            # Check for layout issues
            scroll_width = page.evaluate("document.documentElement.scrollWidth")
            if scroll_width > width:
                print(f"  ⚠ OVERFLOW detected: {scroll_width}px > {width}px")
            
            # Capture screenshot
            if screenshot_name == "mobile-menu":
                page.click(".menu-btn")
                page.screenshot(path=str(OUTPUT_DIR / f"{screenshot_name}.png"))
            else:
                page.screenshot(
                    path=str(OUTPUT_DIR / f"{screenshot_name}.png"),
                    full_page=True
                )
            
            # Check for broken images
            broken = page.evaluate(
                "[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src)"
            )
            if broken:
                print(f"  ⚠ BROKEN images: {broken}")
            
            page.close()
        
        browser.close()
    
    print(f"\n✓ Screenshots saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
