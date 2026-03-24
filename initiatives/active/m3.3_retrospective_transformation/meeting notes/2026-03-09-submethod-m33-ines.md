# Sub-method M3.3 drill down with Inês
*2026-03-09*

## Attendees
- @Inês Matos

## Context
M3.3: Clarify Operational Accountability by Refining Triage Models & OLAs
- Ensure formal separation of support cases from service incidents through defined governing mechanisms and OLAs between Support and Engineering

## Notes

### Key Discussion Topics

**1. Salesforce Support Model**
- Proposed model separates services and incidents, based on Salesforce documentation - https://help.salesforce.com/s/articleView?id=service.incident_mgmt_case_vs_incident.htm&type=5 
- Model includes support cases and incidents, with Engineering acting as advanced support line for support cases
- Need to refine proposal, create clear definitions, and develop appropriate workflows for artifact integration
- Concerns about practical implementation, especially managing transition from incidents to support cases when necessary

**2. Separation of Rituals and Artifacts**
- Retrospectives should be treated as mandatory rituals after incidents, separate from the artifacts that manage them
- Artifacts must be controlled and measured appropriately
- Review existing diagram showing integration between all artifacts - https://outsystemsrd.atlassian.net/wiki/spaces/RKB/pages/4977361294/Incident+Response+Process

**3. Action Items Organization (Salesforce)**
- Need better understanding of which elements are rituals vs. artifacts in the system
- Proposal to review previous Sara conversations and adapt to Salesforce model
- Current heuristic is defined but needs validation
- Processes are too high-level and need more detail
- Importance of validating heuristic and clearly defining organic streams


## Action Items and tasks to include on the project
### Vera
- [ ] Consult Valentim about probability and handling of incident demotion to support case, discuss theoretical and practical approach for these cases
- [ ] Retrieve previous conversations and diagrams (e.g., Lucid Charts diagram) to serve as basis for new artifact integration proposal - https://lucid.app/lucidchart/1d1d7b4c-0070-4dfa-b094-f408ebc3b27d/edit?invitationId=inv_224533ce-c8a3-40c6-9240-f096393da555&referringApp=slack&page=ioy.g1lc27aq#


### Inês
- [ ] Verify and ensure access to display channel and Slack to understand communication flows between Engineering and Support
- [ ] Refine classification and support/incident process model, aligning with Salesforce model and including Core User Journey layer
- [ ] Validate and detail heuristic for differentiating support case vs. service incident
- [ ] Create or update workflow diagrams and artifact architecture, showing integration between all artifacts (cases, incidents, problem records, action items) and associated rituals (retrospectives)
- [ ] Implement control mechanisms to ensure retrospectives and identified problems are conducted and monitored, especially within problem management scope (method 3.4)
- [ ] Ensure support has mechanisms to declare service incident earlier, including defining flows and integration between Engineering and Support (e.g., Slack button/form to trigger Zendesk communications)
- [ ] Define and document clear criteria for incident definition (e.g., affects multiple customers) and support case, aligning with Salesforce examples
- [ ] Review and, if necessary, update retrospective mechanisms, ensuring it's a mandatory ritual after service incidents, with appropriate structure and review
- [ ] Ensure proposal includes follow-up mechanisms for customers, especially in service incident cases, ensuring effective communication and customer unblocking

