#!/usr/bin/env python3
"""
Export Confluence page hierarchy to markdown

Usage:
    python tools/export-confluence-hierarchy.py <page_id> <output_dir>

Example:
    python tools/export-confluence-hierarchy.py 3071508734 docs/processes/odc
"""

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import re


def get_credentials():
    """Get Confluence credentials from environment"""
    url = os.getenv("CONFLUENCE_URL", "https://outsystemsrd.atlassian.net/wiki")
    username = os.getenv("CONFLUENCE_USERNAME")
    token = os.getenv("CONFLUENCE_API_TOKEN")

    if not username or not token:
        print("Error: Set CONFLUENCE_USERNAME and CONFLUENCE_API_TOKEN environment variables")
        sys.exit(1)

    return url, HTTPBasicAuth(username, token)


def sanitize_filename(title):
    """Convert page title to safe filename"""
    # Remove special characters, replace spaces with hyphens
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-') + '.md'


def get_user_display_name(confluence_url, auth, account_id):
    """Fetch user display name by account ID"""
    try:
        endpoint = f"{confluence_url}/rest/api/user"
        params = {"accountId": account_id}
        response = requests.get(endpoint, params=params, auth=auth, timeout=5)
        response.raise_for_status()
        user = response.json()
        return user.get("displayName", user.get("publicName", account_id))
    except:
        # If fetch fails, return account ID
        return account_id


def html_to_markdown(html, confluence_url=None, auth=None):
    """Basic HTML to Markdown conversion with user mention support"""
    # This is simplified - for production use a proper library like markdownify
    md = html

    # Cache for user display names to avoid repeated API calls
    user_cache = {}

    # Headers
    md = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', md)
    md = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', md)
    md = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', md)
    md = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', md)

    # Bold and italic
    md = re.sub(r'<strong>(.*?)</strong>', r'**\1**', md)
    md = re.sub(r'<b>(.*?)</b>', r'**\1**', md)
    md = re.sub(r'<em>(.*?)</em>', r'*\1*', md)
    md = re.sub(r'<i>(.*?)</i>', r'*\1*', md)

    # Links
    md = re.sub(r'<a href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', md)

    # Lists
    md = re.sub(r'<ul[^>]*>', '\n', md)
    md = re.sub(r'</ul>', '\n', md)
    md = re.sub(r'<li[^>]*>', '- ', md)
    md = re.sub(r'</li>', '\n', md)

    # Paragraphs
    md = re.sub(r'<p[^>]*>', '\n', md)
    md = re.sub(r'</p>', '\n', md)
    md = re.sub(r'<br\s*/?>', '\n', md)

    # Code
    md = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', md)
    md = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', md, flags=re.DOTALL)

    # Confluence user mentions - extract display name or username
    # Pattern 1: <ac:link><ri:user .../></ac:link> with optional display name
    def replace_user_mention(match):
        content = match.group(0)
        # Try to extract display name from <ac:plain-text-link-body>
        display_name_match = re.search(r'<ac:plain-text-link-body><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>', content)
        if display_name_match:
            return display_name_match.group(1)

        # Try account-id (fetch from API)
        account_id_match = re.search(r'ri:account-id="([^"]+)"', content)
        if account_id_match:
            account_id = account_id_match.group(1)
            if account_id in user_cache:
                return user_cache[account_id]
            if confluence_url and auth:
                display_name = get_user_display_name(confluence_url, auth, account_id)
                user_cache[account_id] = display_name
                return display_name
            return account_id

        # Fall back to username from ri:username attribute
        username_match = re.search(r'ri:username="([^"]+)"', content)
        if username_match:
            username = username_match.group(1)
            # Convert username to display name format (john.doe -> John Doe)
            return username.replace('.', ' ').replace('-', ' ').title()
        return ''

    md = re.sub(r'<ac:link[^>]*>.*?<ri:user[^>]*/>.*?</ac:link>', replace_user_mention, md, flags=re.DOTALL)

    # Pattern 2: Direct <ri:user> tags without ac:link wrapper (username)
    def replace_direct_user(match):
        username = match.group(1)
        return username.replace('.', ' ').replace('-', ' ').title()

    md = re.sub(r'<ri:user[^>]*ri:username="([^"]+)"[^>]*/>', replace_direct_user, md)

    # Pattern 3: User mentions with account-id (fetch display name from API)
    def replace_account_id_mention(match):
        account_id = match.group(1)
        if account_id in user_cache:
            return user_cache[account_id]
        if confluence_url and auth:
            display_name = get_user_display_name(confluence_url, auth, account_id)
            user_cache[account_id] = display_name
            return display_name
        return account_id

    md = re.sub(r'<ri:user[^>]*ri:account-id="([^"]+)"[^>]*/>', replace_account_id_mention, md)

    # Remove remaining HTML tags
    md = re.sub(r'<[^>]+>', '', md)

    # Clean up extra whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)

    return md.strip()


def get_child_pages(confluence_url, auth, page_id):
    """Get all child pages of a given page"""
    endpoint = f"{confluence_url}/rest/api/content/{page_id}/child/page"
    params = {"limit": 100}

    response = requests.get(endpoint, params=params, auth=auth)
    response.raise_for_status()

    result = response.json()
    return result.get("results", [])


def export_page(confluence_url, auth, page_id, output_dir, depth=0):
    """Export a page and its children to markdown"""

    # Fetch page content
    endpoint = f"{confluence_url}/rest/api/content/{page_id}"
    params = {"expand": "body.storage,version,space,ancestors"}

    print(f"{'  ' * depth}Fetching page {page_id}...")
    response = requests.get(endpoint, params=params, auth=auth)
    response.raise_for_status()

    page = response.json()

    # Extract metadata
    title = page["title"]
    page_url = f"{confluence_url}{page['_links']['webui']}"
    version = page["version"]["number"]
    space = page["space"]["key"]
    body_html = page["body"]["storage"]["value"]

    # Convert to markdown
    body_md = html_to_markdown(body_html, confluence_url, auth)

    # Create frontmatter
    frontmatter = f"""---
title: {title}
confluence_url: {page_url}
confluence_space: {space}
confluence_page_id: {page_id}
last_synced: {datetime.now().strftime("%Y-%m-%d")}
owner: Process Engineering
---

"""

    # Combine
    markdown_content = frontmatter + f"# {title}\n\n" + body_md

    # Determine output path
    filename = sanitize_filename(title)
    output_path = os.path.join(output_dir, filename)

    # Write to file
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"{'  ' * depth}OK Exported: {filename}")

    # Export children
    children = get_child_pages(confluence_url, auth, page_id)
    for child in children:
        child_id = child["id"]
        export_page(confluence_url, auth, child_id, output_dir, depth + 1)


def main():
    if len(sys.argv) != 3:
        print("Usage: python export-confluence-hierarchy.py <page_id> <output_dir>")
        print("Example: python export-confluence-hierarchy.py 3071508734 docs/processes/odc")
        sys.exit(1)

    page_id = sys.argv[1]
    output_dir = sys.argv[2]

    confluence_url, auth = get_credentials()

    print(f"Exporting page {page_id} and children to {output_dir}/")
    print("-" * 60)

    export_page(confluence_url, auth, page_id, output_dir)

    print("-" * 60)
    print(f"OK Export complete!")


if __name__ == "__main__":
    main()
