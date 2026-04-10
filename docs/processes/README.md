# Process Engineering Documentation

This directory contains markdown versions of Process Engineering documentation from Confluence, making it easier to:
- Version control process changes
- Search and reference locally
- Use with Claude Code skills
- Review changes via PRs

## Structure

```
processes/
├── incident-response/      # Incident Response procedures
├── change-management/      # RFC, CAB, reviewers
├── problem-management/     # Root cause analysis
├── failure-management/     # Failure handling
├── access-management/      # PIM permissions
└── special-procedures/     # One-off procedures
```

## Source of Truth

**Confluence remains the source of truth.** These markdown files are exports for local reference and Claude Code integration.

When updating:
1. Update Confluence first
2. Export to markdown
3. Commit to this repo
4. Include Confluence URL in frontmatter

## Format

Each markdown file should include frontmatter:

```markdown
---
title: Page Title
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/...
last_updated: 2026-04-09
owner: Process Engineering
---

# Content here
```

## How to Export from Confluence

### Manual Export
1. Go to Confluence page
2. Click "..." → Export → Markdown
3. Save to appropriate subdirectory
4. Add frontmatter
5. Commit

### Automated Export (Future)
Create a script that uses Confluence API to export pages automatically.

## Usage with Claude Code

Use the `/pe-processes` skill to ask questions about processes. Claude will search these markdown files and provide answers.

Example:
```
You: How do I escalate to O11?
Claude: [Searches docs/processes/incident-response/o11-escalation-bridge.md]
```

## Contributing

When adding new process documentation:
1. Create markdown file in appropriate subdirectory
2. Include frontmatter with Confluence URL
3. Use clear headers and structure
4. Include examples where helpful
5. Submit PR for review

## Owners

- **Vera Branco** - Team Lead, Process Engineering
- **Process Engineering Team** - Inês Matos, Laura Ferreira, Paulo Alves Monteiro
