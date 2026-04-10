#!/usr/bin/env python3
"""
Export Confluence pages to markdown for local documentation

Usage:
    python tools/export-confluence-to-md.py <page_id> <output_path>

Example:
    python tools/export-confluence-to-md.py 6192431127 docs/processes/access-management/pim-permissions.md
"""

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


def export_page(page_id: str, output_path: str):
    """Export a Confluence page to markdown"""

    # Get credentials from environment
    confluence_url = os.getenv("CONFLUENCE_URL", "https://outsystemsrd.atlassian.net/wiki")
    username = os.getenv("CONFLUENCE_USERNAME")
    token = os.getenv("CONFLUENCE_API_TOKEN")

    if not username or not token:
        print("Error: CONFLUENCE_USERNAME and CONFLUENCE_API_TOKEN must be set")
        sys.exit(1)

    auth = HTTPBasicAuth(username, token)

    # Fetch page content
    endpoint = f"{confluence_url}/rest/api/content/{page_id}"
    params = {"expand": "body.storage,version,space"}

    print(f"Fetching page {page_id}...")
    response = requests.get(endpoint, params=params, auth=auth)
    response.raise_for_status()

    page = response.json()

    # Extract metadata
    title = page["title"]
    page_url = f"{confluence_url}{page['_links']['webui']}"
    version = page["version"]["number"]
    space = page["space"]["key"]
    body = page["body"]["storage"]["value"]

    # Create frontmatter
    frontmatter = f"""---
title: {title}
confluence_url: {page_url}
confluence_space: {space}
confluence_version: {version}
last_updated: {datetime.now().strftime("%Y-%m-%d")}
owner: Process Engineering
---

"""

    # Basic HTML to Markdown conversion (simplified)
    # For production, use a proper HTML to Markdown library like markdownify
    markdown_body = body
    markdown_body = markdown_body.replace("<p>", "\n").replace("</p>", "\n")
    markdown_body = markdown_body.replace("<strong>", "**").replace("</strong>", "**")
    markdown_body = markdown_body.replace("<em>", "*").replace("</em>", "*")
    markdown_body = markdown_body.replace("<br/>", "\n").replace("<br>", "\n")

    # Combine
    markdown_content = frontmatter + f"# {title}\n\n" + markdown_body

    # Write to file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"✓ Exported to: {output_path}")
    print(f"  Title: {title}")
    print(f"  Space: {space}")
    print(f"  Version: {version}")
    print(f"  URL: {page_url}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export-confluence-to-md.py <page_id> <output_path>")
        print("Example: python export-confluence-to-md.py 6192431127 docs/processes/access-management/pim-permissions.md")
        sys.exit(1)

    page_id = sys.argv[1]
    output_path = sys.argv[2]

    export_page(page_id, output_path)
