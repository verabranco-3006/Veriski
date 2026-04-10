#!/usr/bin/env python3
import re

# Sample HTML from actual page
html = '''<td ac:local-id="08fce68d-c955-49f9-abac-766a070ff164"><p local-id="272925ca113c"><ac:link><ri:user ri:account-id="603cbdeeee11770070461acc" ri:local-id="897783fa-26ef-435d-9a50-04bbb387f201" /></ac:link> </p></td>'''

print("Original HTML:")
print(html)
print("\n" + "="*60)

# Test regex pattern
pattern = r'<ri:user[^>]*ri:account-id="([^"]+)"[^>]*/>'
matches = re.findall(pattern, html)

print(f"\nMatches found: {len(matches)}")
print(f"Account IDs: {matches}")

# Test replacement
def replace_account_id(match):
    account_id = match.group(1)
    return f"[USER:{account_id}]"

result = re.sub(pattern, replace_account_id, html)
print(f"\nAfter replacement:")
print(result)
