# Process Engineering Documentation Index

**Last Updated:** 2026-04-09 (CAB Constituency added)
**Total Files:** 224 (188 ODC + 36 O11)

This index maps process questions to specific documentation files.

---

## 1. Change Management

### 1.1 Overview & Quick Reference
- **Cheat Sheet** (START HERE for change questions)
  - File: `docs/processes/odc/change-management-cheat-sheet.md`
  - Contains: Flowchart, summary table of Standard/Normal/Emergency changes
  - Key Content:
    - Standard Change (lines 33-56): Pre-approved, low risk, must be in catalog
    - Normal Change (lines 58-78): Planned, CAB approval required, medium/high risk
    - Emergency Change (lines 80-103): Immediate action, high/critical risk, VS Leader approval
  - Best for: Quick comparison of change types

- **Main Process**
  - File: `docs/processes/odc/change-management-process.md`
  - Contains: Full change management workflow
  - Note: May be mostly empty from export - check cheat sheet first

### 1.2 Change Types & Forms

#### Emergency Changes
**CRITICAL CONTEXT:** Only for system-wide impact (Scenario 2)

- **When to Use:**
  - File: `docs/processes/odc/change-management-cheat-sheet.md` (lines 80-103)
  - Context: Immediate action needed, critical issues, positive rings
  - Risk: High/Critical
  - Approval: VS Leader written approval (Slack/Jira) required BEFORE implementation

- **How to Create:**
  - File: `docs/processes/odc/scenario-2-incident-with-system-wide-impact.md` (lines 89-106)
  - Jira Project: **RFC**
  - Form: https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/3/12524
  - Assignment: Add `SRE Global` to Teams field to trigger SRE
  - Post-implementation: Root Cause Analysis required (via Incident Retrospective)

- **Template:**
  - File: `docs/processes/odc/template-standardnormalemergency-document-a-new-change.md`
  - Sections: Summary, General Info, Pre-requisites, Implementation Plan, Rollback

#### Normal Changes
- **When to Use:**
  - File: `docs/processes/odc/change-management-cheat-sheet.md` (lines 58-78)
  - Context: Planned, not urgent, requires formal approval
  - Risk: Medium/High
  - Approval: CAB required
  - Catalog: Must have catalog article

- **How to Create:**
  - File: `docs/processes/odc/scenario-1-incident-without-system-wide-impact.md` (lines 137-143)
  - OR: `docs/processes/odc/scenario-2-incident-with-system-wide-impact.md` (lines 94-100)
  - Jira Project: **RFC**
  - Form: https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/2/12523

#### Standard Changes
- **When to Use:**
  - File: `docs/processes/odc/change-management-cheat-sheet.md` (lines 33-56)
  - Context: Pre-approved, repeatable, well-documented, low risk
  - Approval: Pre-approved (no CAB needed)
  - Catalog: MUST be listed in Change Catalog

- **How to Create:**
  - File: `docs/processes/odc/scenario-1-incident-without-system-wide-impact.md` (line 137)
  - OR: `docs/processes/odc/scenario-2-incident-with-system-wide-impact.md` (line 94)
  - Jira Project: **RFC**
  - Form: https://outsystemsrd.atlassian.net/jira/software/c/projects/RFC/forms/form/direct/6/12582

- **Approved List:**
  - File: `docs/processes/odc/list-of-approved-standard-changes.md`
  - Contains: All pre-approved standard changes

- **Catalog:**
  - File: `docs/processes/odc/odc-change-catalog.md`
  - Contains: Full catalog of changes

### 1.3 Special Change Procedures
- **Major Updates:**
  - File: `docs/processes/odc/major-updates-special-procedure.md`
  - Context: Raised as Normal Changes via RFCD Project form
  - Reviewer: Auto-assigned

- **LaunchDarkly Feature Toggles:**
  - File: `docs/processes/odc/launch-darkly-feature-toggles-change-management.md`

### 1.4 Change Metrics
- **Change Failure Rate:**
  - File: `docs/processes/odc/measuring-change-failure-rate.md`
  - Contains: How RFC changes are measured

### 1.5 Updates & Release Notes
- **Recent Changes:**
  - File: `docs/processes/odc/change-management-release-notes.md`
  - File: `docs/processes/odc/updates-to-rfc-and-rdinc-jira-projects.md`

### 1.6 CAB Process & Approvers
- **CAB Process Overview:**
  - File: `docs/processes/odc/v6-cab-process.md`
  - Confluence: https://outsystemsrd.atlassian.net/wiki/spaces/EEO/pages/5828477154
  - Contains: CAB goals, roles, procedures, meeting process
  - Key Roles:
    - **Change Reviewers**: Perform formal review, advise approvers, oppose if needed
    - **Change Approvers**: Approve Normal and Emergency changes
    - **VS Leaders**: Minimum level to approve Emergency Changes

- **CAB Constituency** (lines 211-294):
  - **Cloud Platform**: Renato Armani (VS Lead), Tiago Oliveira (Fallback)
  - **Migrations**: João Lopes Batista (VS Lead), Filipe Rodrigues (Fallback)
  - **PaaS**: Anand Yashwanth Kumar Santhanam (VS Lead), João Rodrigues (Fallback)
    - PaaS Services/RDO: Laura Huysamen
    - Self-hosted: Sérgio Almeida
    - Tenant LifeCycle: Marco Alves
  - **Agentic Apps & Data**: Sudharshan Krishnamurthy (VS Lead), Hugo Gaspar et al. (Fallback)
  - **AI**: João Ascensão (VS Lead), Kapil Jaisinghani / Pedro Resende / Ambarish Kumar (Fallback)
  - **ALM**: Rui Santos (VS Lead), Sara Gonçalves (Fallback)
  - **Identity**: Nuno Parreira (VS Lead), Francisco Oliveira (Fallback)
  - **Mobile**: Vitor Oliveira (VS Lead), Luís Raposo Silva (Fallback)
  - **Morpheus**: Miguel Rebelo (VS Lead), Bruno Cunha e Silva (Fallback)
  - **Release Engineering**: João Brandão (VS Lead), João Figueira Gomes (Fallback)
  - **SRE & Monitoring & Observability**: Pedro Charola Alves (VS Lead), Tiago Garcia / Nishit Dalal (Fallback)

- **CAB Meeting Logs:**
  - File: `docs/processes/odc/cab-meeting-notes.md`
  - File: `docs/processes/odc/2024-odc-cab-meeting-log.md`
  - File: `docs/processes/odc/2025-odc-cab-meeting-log.md`

---

## 2. Incident Response

### 2.1 Overview
- **Main Process:**
  - File: `docs/processes/odc/incident-response-process.md`
  - Contains: High-level flow, scenario definitions
  - Key Definitions:
    - System-wide impact: 1+ regions, >1 tenant affected
    - Without system-wide impact: 1 tenant only

- **Cheat Sheet:**
  - File: `docs/processes/odc/incident-response-and-collaboration-cheat-sheet.md`

- **What's New:**
  - File: `docs/processes/odc/whats-new-on-incident-response.md`

### 2.2 Incident Scenarios

**CRITICAL:** Choose the RIGHT scenario based on impact

#### Scenario 1: WITHOUT System-Wide Impact
- **File:** `docs/processes/odc/scenario-1-incident-without-system-wide-impact.md`
- **When:** 1 tenant only, partial or full disruption
- **Severity:** Typically Sev 3, Sev 4
- **Team:** Development Team (not SRE)
- **RFC Forms:** Standard/Normal/Emergency (lines 137-143)
- **Key Sections:**
  - Initial Troubleshooting (how to swarm with teams)
  - How to engage Global Support
  - Recovery measures (rollback, other mitigations)

#### Scenario 2: WITH System-Wide Impact
- **File:** `docs/processes/odc/scenario-2-incident-with-system-wide-impact.md`
- **When:** 1+ regions, >1 tenant affected
- **Severity:** Typically Sev 1, some Sev 2
- **Team:** SRE Team (Incident Commander)
- **RFC Forms:** Standard/Normal/Emergency (lines 94-106)
- **Key Sections:**
  - Incident Declaration by SRE
  - Communication Lead assigned
  - Recovery measures with SRE involvement

#### Scenario 3: Late Detection of System-Wide Impact
- **File:** `docs/processes/odc/scenario-3-incident-with-late-detection-of-system-wide-impact.md`
- **When:** Started as Scenario 1, escalated to system-wide
- **RFC Forms:** Standard/Normal/Emergency (lines 149-155)

### 2.3 Jira Workflows
- **What Incidents Look Like:**
  - File: `docs/processes/odc/what-does-an-odc-incident-look-like-in-jira.md`
  - Project: **RDINC**
  - Mandatory fields for Change Failure Rate tracking

- **RDINC Workflow & Statuses:**
  - File: `docs/processes/odc/rdinc-workflow-and-statuses.md`

- **Handling Duplicates:**
  - File: `docs/processes/odc/handling-duplicate-incidents-in-jira.md`

### 2.4 Guidelines & Templates
- **Creating Incidents from Alerts:**
  - File: `docs/processes/odc/guideline-creating-incidents-from-alerts.md`

- **Communication Templates:**
  - File: `docs/processes/odc/incidents-communication-templates.md`

- **Internal Communication (System-Wide):**
  - File: `docs/processes/odc/internal-communication-of-incidents-with-system-wide-impact.md`
  - File: `docs/processes/odc/action-guide-for-internal-communications-leader.md`
  - File: `docs/processes/odc/notify-internal-communications-leader-upon-incident-declaration.md`

### 2.5 Special Procedures

#### O11 Escalation Bridge
**CRITICAL:** For escalating ODC incidents to O11

- **ODC Version:**
  - File: `docs/processes/odc/special-procedure-o11-odc-escalation-bridge.md`
  - Confluence: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/5959745558
  - When: Dependency on O11 during ODC incident
  - How: Set "Is an O11 Escalation Needed?" to Yes on RDINC Troubleshooting tab
  - Auto-actions: Creates RDSC ticket, notifies Global Support, RDINC → Solved
  - Slack: #odc_o11_escalation_bridge

- **O11 Version:**
  - File: `docs/processes/o11/special-procedure-o11-odc-escalation-bridge.md`

- **Sample File (Manual):**
  - File: `docs/processes/incident-response/o11-escalation-bridge.md`

### 2.6 Rootly Integration
- **Get to Know Rootly:**
  - File: `docs/processes/odc/get-to-know-rootly.md`

### 2.7 Product Areas & Error Codes
- **PACA Updates:**
  - File: `docs/processes/odc/product-areas-error-codes-updates-on-odc.md`
  - Contains: Emergency change requests for PACA structure
  - Template for emergency PACA changes

---

## 3. Retrospectives (Post-Incident)

### 3.1 Main Process
- **Overview:**
  - File: `docs/processes/odc/retrospective-process.md`
  - Scope: Mandatory for system-wide impact incidents
  - Owner: SRE Team (RCA Commanders), handoff to Process Engineering
  - Jira: Managed in RDINC Incident issue, "Retrospective" tab

- **Template:**
  - File: `docs/processes/odc/template-retrospective-document.md`

### 3.2 Database
- **All Retrospectives:**
  - File: `docs/processes/odc/retrospectives-database.md`
  - File: `docs/processes/odc/incident-retrospectives-database.md`
  - Contains: Links to all completed retrospectives

### 3.3 Example Retrospectives
All retrospective files follow pattern: `retrospective-sev[1-4]-*.md`
- Location: `docs/processes/odc/retrospective-sev*.md`
- Use for reference on format and depth

---

## 4. Problem Management

### 4.1 ODC Problem Records (RPMs)
- **Creation Process:**
  - File: `docs/processes/odc/odc-problem-records-odc-rpms-creation.md`

- **Priority Matrix:**
  - File: `docs/processes/odc/odc-rpms-priority-matrix.md`

---

## 5. Failure Management

### 5.1 CD Failures
- **Overview:**
  - File: `docs/processes/odc/failure-management.md`
  - Project: **RDODCF** (ODC CD Failures)
  - Context: Deployment failures on Pegasus
  - Separation from RDINC to avoid label confusion

- **What CD Failures Look Like:**
  - File: `docs/processes/odc/what-does-an-odc-cd-failure-look-like-in-jira.md`

---

## 6. PIM / Access Management

### 6.1 Permission Sets
- **Main Documentation:**
  - File: `docs/processes/odc/permission-sets-in-pim.md`
  - Confluence: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/6192431127
  - Context: Centralized documentation created with IAM team (Carlos Marques)
  - Status: As-is implementation, updated as changes occur
  - **NOTE:** Exported file may be empty - refer to Confluence URL

- **Sample File (Manual):**
  - File: `docs/processes/access-management/pim-permissions.md`

### 6.2 Infrastructure Access
- **Destructive Operations:**
  - File: `docs/processes/odc/guideline-destructive-level-operations-permissions.md`

- **Rings Access:**
  - File: `docs/processes/odc/how-to-access-the-rings-infrastructure.md`
  - File: `docs/processes/odc/how-to-run-sql-queries-in-platform-dbs.md`

---

## 7. O11 Support Process

### 7.1 Overview
- **Main Process:**
  - File: `docs/processes/o11/support-process.md`
  - Confluence: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/726335551

- **High-Level Lifecycle:**
  - File: `docs/processes/o11/support-cases-high-level-lifecycle.md`

- **Case Distribution:**
  - File: `docs/processes/o11/support-case-distribution-inside-rd.md`

### 7.2 Working with Support Cases
- **In Jira:**
  - File: `docs/processes/o11/support-cases-in-jira.md`

- **Communication:**
  - File: `docs/processes/o11/communication-in-support-cases.md`

- **Priorities & OLAs:**
  - File: `docs/processes/o11/support-cases-priorities-and-olas.md`

- **Tips:**
  - File: `docs/processes/o11/tip-for-working-support-cases.md`

- **Rotations:**
  - File: `docs/processes/o11/support-rotations.md`

### 7.3 Creating Defects
- **From Support Cases:**
  - File: `docs/processes/o11/creating-a-defect-from-support-cases.md`

- **Poorly Escalated Cases:**
  - File: `docs/processes/o11/poorly-escalated-support-cases.md`

### 7.4 Troubleshooting Guides
- **Memory:**
  - File: `docs/processes/o11/memory-troubleshooting.md`

- **Performance:**
  - File: `docs/processes/o11/performance-troubleshooting.md`

- **Solution Publish:**
  - File: `docs/processes/o11/what-is-solution-publish-and-what-makes-it-tick.md`
  - File: `docs/processes/o11/faq-troubleshooting-solution-publish.md`
  - File: `docs/processes/o11/solution-publish-database-tables.md`

- **FICO:**
  - File: `docs/processes/o11/how-to-handle-and-troubleshoot-fico-support-cases.md`

- **Database:**
  - File: `docs/processes/o11/database.md`
  - File: `docs/processes/o11/oracle.md`
  - File: `docs/processes/o11/retrieving-files-from-the-database-binaries.md`

- **Deploy Service:**
  - File: `docs/processes/o11/deploy-service.md`

- **Processes & Crashes:**
  - File: `docs/processes/o11/processes-crashes-and-other-behaviors-in-sentry-machines.md`

### 7.5 FAQs & Resources
- **Encryption & Passwords:**
  - File: `docs/processes/o11/faq-about-encryption-passwords-confidential-information-and-other-related-topics.md`

- **Cookies & Sessions:**
  - File: `docs/processes/o11/faq-about-cookies-and-session.md`

- **Template Responses:**
  - File: `docs/processes/o11/template-responses.md`

- **Useful Tools:**
  - File: `docs/processes/o11/useful-tools.md`

- **Resource Index:**
  - File: `docs/processes/o11/resource-index.md`

- **Logging:**
  - File: `docs/processes/o11/working-with-logging.md`

### 7.6 Permissions & Applications
- **Permission Model:**
  - File: `docs/processes/o11/applications-permission-model.md`

### 7.7 R&D Specific
- **Incident Management FAQs:**
  - File: `docs/processes/o11/rd-incident-management-faqs.md`

- **Support Pods:**
  - File: `docs/processes/o11/rd-support-pods.md`

- **Incidents with DBA Help:**
  - File: `docs/processes/o11/support-incident-with-dba-help.md`

- **Setup & Best Practices:**
  - File: `docs/processes/o11/setup-and-best-practices.md`

### 7.8 OTA Upgrades
- **Overview:**
  - File: `docs/processes/o11/upgrades-over-the-air-ota-in-o11-overview.md`

---

## 8. Tenant & Environment Management

### 8.1 Tenant Creation
- **Internal Purposes:**
  - File: `docs/processes/odc/tenant-creation-for-internal-purposes.md`

- **Baseline Payloads:**
  - File: `docs/processes/odc/baseline-for-tenant-payloads-provisioning.md`

---

## 9. Cost Management

### 9.1 Cost Anomaly Management
- **Process:**
  - File: `docs/processes/odc/cost-anomaly-management-process.md`

- **What RDCAM Looks Like:**
  - File: `docs/processes/odc/what-does-an-rdcam-look-like-in-jira.md`

---

## 10. CAB & Release Management

### 10.1 CAB Meetings
- **2024 Log:**
  - File: `docs/processes/odc/2024-odc-cab-meeting-log.md`

- **2025 Log:**
  - File: `docs/processes/odc/2025-odc-cab-meeting-log.md`

- **Meeting Notes:**
  - File: `docs/processes/odc/cab-meeting-notes.md`

---

## 11. Jira Notifications

### 11.1 Slack Integration
- **Activate Notifications:**
  - File: `docs/processes/odc/activate-jira-notifications-in-slack.md`

---

## 12. Process Release Notes

### 12.1 Updates
- **All Release Notes:**
  - File: `docs/processes/odc/process-release-notes.md`

---

## Quick Reference by Question Type

### "How do I create/open a [change type]?"
1. Check `change-management-cheat-sheet.md` for change type definition
2. For Emergency: Check `scenario-2-incident-with-system-wide-impact.md` (lines 89-106)
3. For Normal/Standard: Check `scenario-1-incident-without-system-wide-impact.md` (lines 137-143)
4. All use RFC project with different forms

### "What's the difference between [change types]?"
→ `change-management-cheat-sheet.md` (lines 17-103) - has summary table

### "How do I escalate to O11?"
→ `special-procedure-o11-odc-escalation-bridge.md` (ODC or O11 version)

### "What PIM permissions are available?"
→ `permission-sets-in-pim.md` + Confluence URL (file may be empty)

### "How do I handle an incident?"
1. Determine scope: system-wide or single tenant?
2. System-wide → `scenario-2-incident-with-system-wide-impact.md`
3. Single tenant → `scenario-1-incident-without-system-wide-impact.md`

### "What's the retrospective process?"
→ `retrospective-process.md`

### "How do I create a problem record (RPM)?"
→ `odc-problem-records-odc-rpms-creation.md`

### "What are the support case priorities?"
→ `support-cases-priorities-and-olas.md` (O11)

### "Who is the VS Leader for [team/value stream]?" or "Who approves emergency changes for [team]?"
→ `v6-cab-process.md` (lines 211-294) - CAB Constituency table
**Quick lookup:**
- **Identity**: Nuno Parreira (VS Lead), Francisco Oliveira (Fallback)
- **Cloud Platform**: Renato Armani (VS Lead), Tiago Oliveira (Fallback)
- **PaaS**: Anand Yashwanth Kumar Santhanam (VS Lead), João Rodrigues (Fallback)
- **Mobile**: Vitor Oliveira (VS Lead), Luís Raposo Silva (Fallback)
- **SRE**: Pedro Charola Alves (VS Lead), Tiago Garcia / Nishit Dalal (Fallback)
- **ALM**: Rui Santos (VS Lead), Sara Gonçalves (Fallback)
- **AI**: João Ascensão (VS Lead)
- **Release Engineering**: João Brandão (VS Lead)
- **Morpheus**: Miguel Rebelo (VS Lead)
- **Migrations**: João Lopes Batista (VS Lead)
- **Agentic Apps & Data**: Sudharshan Krishnamurthy (VS Lead)

See full list with fallbacks in Section 1.6

---

## Notes for Skill Usage

1. **Always check context** - Emergency changes are ONLY for system-wide impact (Scenario 2)
2. **Files may be empty** - Some complex Confluence pages didn't export well (e.g., PIM permissions)
3. **Multiple versions exist** - Some procedures have ODC and O11 versions
4. **Line numbers are approximate** - From initial analysis, verify when reading
5. **Confluence URLs are canonical** - If file is empty or unclear, direct to Confluence URL in frontmatter

---

## Index Maintenance

**When to update:**
- After re-exporting documentation from Confluence
- When new processes are added
- When file structure changes

**How to update:**
1. Re-run: `python tools/export-confluence-hierarchy.py [page-id] [output-dir]`
2. Review new/changed files
3. Update this index with new mappings
4. Update skill SKILL.md with index changes
