# How to Export Documentation from Confluence

## Prerequisites

Set environment variables:

```bash
export CONFLUENCE_URL=https://outsystemsrd.atlassian.net/wiki
export CONFLUENCE_USERNAME=your.email@outsystems.com
export CONFLUENCE_API_TOKEN=your_api_token
```

Get API token from: https://id.atlassian.com/manage-profile/security/api-tokens

## Export Commands

### ODC Processes

Export all ODC process documentation:

```bash
python tools/export-confluence-hierarchy.py 3071508734 docs/processes/odc
```

Source: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/3071508734/ODC+Processes

### O11 Support Process

Export all O11 support documentation:

```bash
python tools/export-confluence-hierarchy.py 726335551 docs/processes/o11
```

Source: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726335551/Support+Process

## After Export

1. Review the exported markdown files
2. Check that formatting looks correct
3. Commit to Git
4. Test the `/pe-processes` skill with questions

## Re-sync

To update documentation when Confluence changes:

```bash
# Re-run the export commands
python tools/export-confluence-hierarchy.py 3071508734 docs/processes/odc
python tools/export-confluence-hierarchy.py 726335551 docs/processes/o11
```

The script will overwrite existing files with the latest content.

## Troubleshooting

**Authentication errors:**
- Verify CONFLUENCE_USERNAME and CONFLUENCE_API_TOKEN are set
- Check that your token hasn't expired
- Ensure you have access to the RKB and RCP spaces

**Missing pages:**
- Check that the page ID is correct
- Verify you have permission to view the page
- Some pages may be restricted

**Formatting issues:**
- The HTML to Markdown conversion is basic
- For complex pages, you may need to manually edit the markdown
- Consider using a proper library like `markdownify` for better conversion
