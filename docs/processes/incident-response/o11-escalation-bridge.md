---
title: Special Procedure - O11 ODC Escalation Bridge
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/[ID]
last_updated: 2026-04-09
owner: Process Engineering
status: Live
---

# Special Procedure | O11 - ODC Escalation Bridge

This procedure handles engineering escalations from ODC to O11, designed to stabilize incident flow following O11 Connector GA and improve cross-platform efficiency.

## Goals

1. **MTTR Protection** - Ensure ODC metrics aren't penalized for platform-side investigations. RDINC transitions to Solved automatically when O11 escalation is triggered.

2. **Direct Handover** - Bypass manual Global Support bottleneck. ODC Engineers can trigger O11 Incident Management directly through Jira.

3. **Strategic Alignment** - Tactical bridge serving as mitigation while broader efforts toward platform unification continue under CPTO Method 4.

## How It Works

### When to Escalate

Use this procedure when:
- You've identified a dependency on O11 during ODC incident investigation
- The issue requires O11 team investigation or action
- You've verified no prior escalation exists for this issue

### Steps

1. **Verify** - Check that no prior escalation exists
2. **Trigger** - Set the field "Is an O11 Escalation Needed?" to **Yes** on your RDINC Troubleshooting tab
3. **Automatic Actions**:
   - System creates and links an RDSC ticket for O11 team
   - Global Support is notified
   - Your RDINC ticket transitions to Solved status

### Communication

For direct technical alignment with O11 during an active escalation:
- Use **#odc_o11_escalation_bridge** Slack channel

## Documentation & Support

- **Playbook**: Full procedure in R&D Knowledge Base
- **Sync Channel**: #odc_o11_escalation_bridge

## Strategic Context

This tactical bridge addresses immediate friction between platforms. Full process unification is handled within CPTO Method 4: "Deliver on our promise of one unified OutSystems platform, bringing O11 and ODC together into one seamless, AI-powered, cloud-native platform."

## Related

- Incident Response playbook
- O11/ODC unification roadmap
- CPTO Method 4 documentation
