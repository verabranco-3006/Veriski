# Response to Aprio Service Incident Sampling Follow-Up Questions

**Date:** April 8, 2026
**Prepared by:** Vera Branco, Process Engineering
**Reference:** ODC A 1.1-01 Follow Ups - 04.07.2026

---

## Question 1: Cancelled Rootly Incidents

**Tickets:** RDINC-73096, RDINC-68883, RDINC-68232, RDINC-67670, RDINC-67620, RDINC-67614, RDINC-67598

These incidents were created during initial triage but cancelled after investigation determined they did not meet service incident criteria.

**Recommendation:** Add `Rootly Status` field to sampling criteria and exclude `Rootly Status = "Cancelled"`.

---

## Question 2: RDINC-68044

This incident was investigated and determined to be a spike (transient issue with no sustained impact). Investigation evidence exists in Slack coordination channel and Rootly incident record. The Jira ticket was not updated after investigation concluded.

**Available evidence:** Slack thread export and Rootly incident record showing investigation and outcome.

---

## Question 3: RDINC-65994

This incident was investigated and determined not to have system-wide impact. The incident was resolved and marked as **Solved in Rootly on December 10, 2025**. The Jira ticket status was not updated.

**Available evidence:** Rootly incident record with December 10, 2025 resolution timestamp and Slack investigation thread.

---

## Root Cause (Questions 2 & 3)

Rootly does not automatically sync incident status or resolution to Jira. Incident response occurs in Rootly and Slack, but Jira status requires manual updates. This integration gap is a known issue currently being addressed.


