#!/usr/bin/env python3
"""Export remaining RFC tickets to PDF for SOC2 CAB Approval Evidence"""

import time
from playwright.sync_api import sync_playwright

missing_rfcs = [
    'RFC-2704', 'RFC-2901', 'RFC-2986', 'RFC-2993',
    'RFC-3134', 'RFC-3136', 'RFC-3437', 'RFC-3443',
    'RFC-3640', 'RFC-3691', 'RFC-4213', 'RFC-4332'
]

def export_rfcs():
    with sync_playwright() as p:
        # Use existing browser context if available, otherwise launch new
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        if not browser:
            browser = p.chromium.launch(headless=False)

        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[0] if context.pages else context.new_page()

        success_count = 0
        fail_count = 0

        for rfc in missing_rfcs:
            try:
                print(f"Exporting {rfc}...")

                # Navigate to RFC
                page.goto(f'https://outsystemsrd.atlassian.net/browse/{rfc}',
                         wait_until='networkidle', timeout=60000)

                # Wait for page to load
                time.sleep(3)

                # Click CAB Review tab if visible
                try:
                    cab_tab = page.locator('tab:has-text("CAB Review")')
                    if cab_tab.is_visible():
                        cab_tab.click()
                        time.sleep(1)
                except:
                    pass  # Tab might not exist or already selected

                # Export to PDF
                page.pdf(
                    path=f'SOC2_CAB_Approval_Evidence/{rfc}.pdf',
                    format='A4',
                    print_background=True,
                    margin={'top': '15mm', 'right': '15mm', 'bottom': '15mm', 'left': '15mm'},
                    scale=0.9
                )

                print(f"✓ {rfc} exported successfully")
                success_count += 1

            except Exception as e:
                print(f"✗ {rfc} failed: {str(e)}")
                fail_count += 1

        print(f"\n=== Export Summary ===")
        print(f"Success: {success_count}")
        print(f"Failed: {fail_count}")
        print(f"Total: {len(missing_rfcs)}")

if __name__ == '__main__':
    export_rfcs()
