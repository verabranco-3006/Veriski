#!/usr/bin/env python3
"""
Test user mention extraction from Confluence HTML
"""

import re


def html_to_markdown(html):
    """Basic HTML to Markdown conversion with user mention support"""
    md = html

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
    # Pattern 1: <ac:link><ri:user ri:username="john.doe"/></ac:link> with optional display name
    def replace_user_mention(match):
        content = match.group(0)
        # Try to extract display name from <ac:plain-text-link-body>
        display_name_match = re.search(r'<ac:plain-text-link-body><!\[CDATA\[(.*?)\]\]></ac:plain-text-link-body>', content)
        if display_name_match:
            return display_name_match.group(1)
        # Fall back to username from ri:username attribute
        username_match = re.search(r'ri:username="([^"]+)"', content)
        if username_match:
            username = username_match.group(1)
            # Convert username to display name format (john.doe -> John Doe)
            return username.replace('.', ' ').replace('-', ' ').title()
        return ''

    md = re.sub(r'<ac:link[^>]*>.*?<ri:user[^>]*/>.*?</ac:link>', replace_user_mention, md, flags=re.DOTALL)

    # Pattern 2: Direct <ri:user> tags without ac:link wrapper
    def replace_direct_user(match):
        username = match.group(1)
        return username.replace('.', ' ').replace('-', ' ').title()

    md = re.sub(r'<ri:user[^>]*ri:username="([^"]+)"[^>]*/>', replace_direct_user, md)

    # Remove remaining HTML tags
    md = re.sub(r'<[^>]+>', '', md)

    # Clean up extra whitespace
    md = re.sub(r'\n{3,}', '\n\n', md)

    return md.strip()


# Test cases
test_cases = [
    {
        "name": "User mention with display name (CDATA)",
        "html": '''<p>Assigned to: <ac:link><ri:user ri:username="john.doe"/><ac:plain-text-link-body><![CDATA[John Doe]]></ac:plain-text-link-body></ac:link></p>''',
        "expected": "Assigned to: John Doe"
    },
    {
        "name": "User mention without display name",
        "html": '''<p>Reviewed by: <ac:link><ri:user ri:username="jane.smith"/></ac:link></p>''',
        "expected": "Reviewed by: Jane Smith"
    },
    {
        "name": "Direct ri:user tag",
        "html": '''<p>Contact: <ri:user ri:username="bob-wilson"/></p>''',
        "expected": "Contact: Bob Wilson"
    },
    {
        "name": "Table with user mentions",
        "html": '''<table>
<tr>
<td>Identity Team</td>
<td><ac:link><ri:user ri:username="alice.jones"/><ac:plain-text-link-body><![CDATA[Alice Jones]]></ac:plain-text-link-body></ac:link></td>
</tr>
<tr>
<td>Platform Team</td>
<td><ac:link><ri:user ri:username="carlos.silva"/></ac:link></td>
</tr>
</table>''',
        "expected_contains": ["Alice Jones", "Carlos Silva"]
    },
    {
        "name": "CAB Constituency table format",
        "html": '''<h2>CAB Constituency</h2>
<table>
<tr>
<th>Value Stream</th>
<th>VS Leader</th>
</tr>
<tr>
<td>Identity</td>
<td><ac:link><ri:user ri:username="pedro.charola"/><ac:plain-text-link-body><![CDATA[Pedro Charola]]></ac:plain-text-link-body></ac:link></td>
</tr>
<tr>
<td>Platform Services</td>
<td><ac:link><ri:user ri:username="joao.rodrigues"/></ac:link></td>
</tr>
</table>''',
        "expected_contains": ["Pedro Charola", "Joao Rodrigues"]
    }
]

print("Testing Confluence User Mention Extraction")
print("=" * 60)

all_passed = True

for i, test in enumerate(test_cases, 1):
    print(f"\nTest {i}: {test['name']}")
    print("-" * 60)

    result = html_to_markdown(test["html"])

    print(f"Input HTML:\n{test['html'][:100]}...")
    print(f"\nOutput Markdown:\n{result}")

    if "expected" in test:
        if result.strip() == test["expected"].strip():
            print("[PASS]")
        else:
            print(f"[FAIL]")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")
            all_passed = False
    elif "expected_contains" in test:
        missing = []
        for expected_str in test["expected_contains"]:
            if expected_str not in result:
                missing.append(expected_str)

        if not missing:
            print("[PASS]")
        else:
            print(f"[FAIL] - Missing: {missing}")
            all_passed = False

print("\n" + "=" * 60)
if all_passed:
    print("[PASS] All tests passed!")
else:
    print("[FAIL] Some tests failed")
