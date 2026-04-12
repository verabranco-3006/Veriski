const fs = require('fs');

// Current Confluence markdown body - read from saved response
// We'll construct the modified body by applying replacements

let body = fs.readFileSync('C:/Users/vbr/Desktop/Veriski/Veriski/temp_confluence_body.md', 'utf8');

// 1. Remove all "✓ FORMAL V2MOM METRIC" labels (with variations)
body = body.replace(/ ✓ FORMAL V2MOM METRIC/g, '');

// 2. Remove all "✓ FOUNDATIONAL METRIC" labels
body = body.replace(/ ✓ FOUNDATIONAL METRIC/g, '');

// 3. Remove M4.3 section entirely (from heading to next ---)
const m43Start = body.indexOf('### M4.3: Dashboard Adoption Rate');
if (m43Start >= 0) {
  // Find the next section after M4.3 (### M4.4)
  const m44Start = body.indexOf('### M4.4:', m43Start);
  if (m44Start >= 0) {
    // Remove from M4.3 heading to just before M4.4 heading
    body = body.substring(0, m43Start) + body.substring(m44Start);
    console.log('Removed M4.3 section');
  }
}

// 4. Update M4.4 status note
body = body.replace(
  '**Status:** Paulo Alves Monteiro to review PE role and metric scope',
  '**Status:** Paulo feedback (April 2026): focus on completeness dimension. Deep dive needed. M4.3 (Dashboard Adoption Rate) removed — leadership consumes metrics via slide decks, not dashboards directly.'
);

// 5. Update summary statistics
body = body.replace('**Total Measurements:** 34', '**Total Measurements:** 33');

body = body.replace(
  `* Formal V2MOM Metrics: 29\n* Foundational Metrics: 4 (M3.4a, M3.4b, M3.4c, M3.4d)\n* Requires Paulo Review: 2 (M4.3, M4.4)\n* Requires Review: 1 (M2.2)`,
  `* Active: 30\n* Requires Paulo Review: 1 (M4.4)\n* Requires Review: 1 (M2.2)\n* Removed: 1 (M4.3)`
);

body = body.replace(
  `* Method 1 (AI Transformation): 4 measurements (4 formal: M1.1a, M1.2a, M1.2b, M1.3a)\n* Method 2 (Change Management): 5 measurements (3 formal)\n* Method 3 (Incident Response): 11 measurements (7 formal + 4 foundational)\n* Method 4 (Metrics Orchestration): 5 measurements (3 formal, 2 requires Paulo review)\n* Method 5 (Team Performance & Development): 5 measurements (5 formal: M5.1a, M5.2a, M5.3a, M5.3b, M5.4a)\n* Method 6 (Operational Excellence): 4 measurements (4 formal)`,
  `* Method 1 (AI Transformation): 4 (M1.1a, M1.2a, M1.2b, M1.3a)\n* Method 2 (Change Management): 4 (M2.1, M2.2, M2.3, M2.4)\n* Method 3 (Incident Response): 11 (M3.1, M3.2, M3.3, M3.4, M3.4a-d, M3.5, M3.6, M3.7)\n* Method 4 (Metrics Orchestration): 3 + 1 requires review (M4.1, M4.2, M4.4, M4.5)\n* Method 5 (Team Performance & Development): 5 (M5.1a, M5.2a, M5.3a, M5.3b, M5.4a)\n* Method 6 (Operational Excellence): 4 (M6.1, M6.2, M6.3, M6.4)`
);

body = body.replace('* Q4 2026: 4 measurements', '* Q4 2026: 3 measurements');

// Write the modified body
fs.writeFileSync('C:/Users/vbr/Desktop/Veriski/Veriski/temp_confluence_body_updated.md', body);
console.log('Done. Body length:', body.length);

// Verify no remaining labels
const formalCount = (body.match(/FORMAL V2MOM METRIC/g) || []).length;
const foundationalCount = (body.match(/FOUNDATIONAL METRIC/g) || []).length;
const m43Count = (body.match(/M4\.3: Dashboard/g) || []).length;
console.log('Remaining FORMAL labels:', formalCount);
console.log('Remaining FOUNDATIONAL labels:', foundationalCount);
console.log('Remaining M4.3 sections:', m43Count);
