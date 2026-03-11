# RFC Testing Evidence - Processing Plan

**Date:** March 11, 2026
**Approach:** Combined evidence package (Jira + Confluence)

---

## Folder Structure

```
SOC2_RFC_Testing_Evidence/
├── RFC-2704/
│   ├── RFC-2704-Jira.pdf
│   └── RFC-2704-Confluence.pdf
├── RFC-2713/
│   ├── RFC-2713-Jira.pdf
│   └── RFC-2713-Confluence.pdf
...
└── RFC-4345/
    ├── RFC-4345-Jira.pdf
    └── RFC-4345-Confluence.pdf
```

---

## Processing Steps

### Step 1: Create folder structure (40 folders)
Create one folder per RFC

### Step 2: Regenerate Jira PDFs with testing evidence visible
For each RFC:
1. Navigate to RFC in Jira
2. Click "General" tab (shows Confluence link + description + testing details)
3. Collapse left sidebar
4. Click "All" in Activity section (shows all comments with testing results)
5. Dual-scroll to top (main window + all scrollable containers)
6. Export to PDF → `RFC-XXXX/RFC-XXXX-Jira.pdf`

### Step 3: Export Confluence catalog articles
For each RFC with Confluence URL:
1. Navigate to Confluence catalog article URL
2. Export page to PDF → `RFC-XXXX/RFC-XXXX-Confluence.pdf`

**Special case:** RFC-4213 has no Confluence article → create `RFC-4213/NO_CONFLUENCE_ARTICLE.txt`

---

## Batch Processing

Process in 4 batches of 10 RFCs each:

### Batch 1 (RFCs 1-10)
RFC-2704, RFC-2713, RFC-2761, RFC-2839, RFC-2901, RFC-2986, RFC-2993, RFC-3134, RFC-3136, RFC-3208

### Batch 2 (RFCs 11-20)
RFC-3437, RFC-3443, RFC-3449, RFC-3465, RFC-3517, RFC-3562, RFC-3639, RFC-3640, RFC-3659, RFC-3691

### Batch 3 (RFCs 21-30)
RFC-3922, RFC-4186, RFC-4213, RFC-4332, RFC-2642, RFC-3061, RFC-3139, RFC-3315, RFC-3375, RFC-3441

### Batch 4 (RFCs 31-40)
RFC-3497, RFC-3527, RFC-3532, RFC-3791, RFC-3865, RFC-3932, RFC-4207, RFC-4235, RFC-4263, RFC-4345

---

## Technical Settings

**Jira PDF:**
- Format: A4
- Scale: 0.7
- Margins: 10mm
- Print background: enabled

**Confluence PDF:**
- Browser print-to-PDF
- Format: A4
- Include all sections

---

## Status Tracking

- [ ] Batch 1 completed
- [ ] Batch 2 completed
- [ ] Batch 3 completed
- [ ] Batch 4 completed
- [ ] All 40 RFC folders ready for auditor

---

**Next:** Create folder structure, then process each batch
