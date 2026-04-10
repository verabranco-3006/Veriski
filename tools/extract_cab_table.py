#!/usr/bin/env python3
import json
import re

with open('C:/Users/vbr/Desktop/cab_page.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

html = data['body']['storage']['value']

# Find the CAB_Constituency section
start = html.find('CAB_Constituency')
if start == -1:
    print("CAB_Constituency not found")
else:
    # Extract a chunk around it
    chunk = html[start:start+5000]

    # Find user mentions in this chunk
    user_mentions = re.findall(r'<ri:user[^>]*ri:userkey="([^"]+)"[^>]*/>', chunk)
    print(f"Found {len(user_mentions)} user mentions")
    print("User keys:", user_mentions[:10])

    # Also look for account IDs
    account_ids = re.findall(r'<ri:user[^>]*ri:account-id="([^"]+)"[^>]*/>', chunk)
    print(f"\nFound {len(account_ids)} account IDs")
    print("Account IDs:", account_ids[:10])

    # Print a sample of the HTML
    print("\n=== Sample HTML ===")
    print(chunk[:2000])
