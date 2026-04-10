# ODC Process Assistant - Simplified Approach

**Status:** Implemented (Tiago's suggestion)
**Approach:** Markdown files in repo + Claude Code skill

---

## What Changed

Original plan was to build a RAG system with vector databases and API calls.

**Tiago's better idea:**
1. Export Confluence pages to markdown in the repo
2. Create a skill that reads those files
3. Claude uses the skill to answer questions
4. No RAG, no APIs, no complexity

## Implementation

### 1. Documentation (docs/processes/)

All Process Engineering documentation is now stored as markdown files:

```
docs/processes/
├── incident-response/
├── change-management/
├── problem-management/
├── failure-management/
├── access-management/
└── special-procedures/
```

### 2. Skill (.claude/skills/pe-processes/)

Created `/pe-processes` skill that tells Claude how to answer process questions using the markdown files.

### 3. Export Tool (tools/export-confluence-to-md.py)

Python script to export Confluence pages to markdown with proper frontmatter.

## How to Use

### Ask Questions

Just ask Claude about processes:

```
"How do I escalate to O11?"
"What's the RFC approval process?"
"What PIM permissions do I need?"
```

Claude will:
1. Search `docs/processes/` for relevant files
2. Read the markdown
3. Answer with citations

### Add Documentation

Export a Confluence page:

```bash
python tools/export-confluence-to-md.py <page_id> docs/processes/<category>/<filename>.md
```

Example:
```bash
python tools/export-confluence-to-md.py 6192431127 docs/processes/access-management/pim-permissions.md
```

## Benefits

✅ Simple - No external dependencies
✅ Version controlled - All docs in Git
✅ Fast - No API calls needed
✅ Offline - Works without internet
✅ Reviewable - Changes via PR
✅ Maintainable - Just markdown files

## Next Steps

1. Export key Confluence pages to markdown
2. Test the `/pe-processes` skill
3. Iterate on skill prompts
4. Add more documentation as needed

## Files

- `.claude/skills/pe-processes/SKILL.md` - The skill
- `docs/processes/` - Process documentation
- `tools/export-confluence-to-md.py` - Export script

---

*Much simpler than the original RAG approach. Thanks Tiago!*
