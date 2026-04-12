const fs = require('fs');
const crypto = require('crypto');

const data = JSON.parse(fs.readFileSync('C:/Users/vbr/.claude/projects/C--Users-vbr-Desktop-Veriski-Veriski/dd64aced-4ddb-441b-bfec-ebd3cedd88e4/tool-results/mcp-claude_ai_Atlassian-getConfluencePage-1776018758135.txt', 'utf8'));
const parsed = JSON.parse(data[0].text);
const adf = parsed.body;

function uid() { return crypto.randomUUID(); }

function mention(accountId, displayName) {
  return { type: "mention", attrs: { id: accountId, localId: uid(), text: "@" + displayName } };
}

function textNode(t, marks) {
  const n = { text: t, type: "text" };
  if (marks) n.marks = marks;
  return n;
}

function paragraph(content, localId) {
  return { type: "paragraph", attrs: { localId: localId || uid().replace(/-/g, '').substring(0, 12) }, content };
}

function heading(level, text) {
  return { type: "heading", attrs: { level, localId: uid().replace(/-/g, '').substring(0, 12) }, content: [textNode(text)] };
}

function rule() {
  return { type: "rule", attrs: { localId: uid() } };
}

function bulletList(items) {
  return {
    type: "bulletList",
    attrs: { localId: uid() },
    content: items.map(itemContent => ({
      type: "listItem",
      attrs: { localId: uid() },
      content: [paragraph(itemContent)]
    }))
  };
}

const INES = "61002179a539cb00682bd680";
const VERA = "6051f3a086b0dd007172caf9";

// === CHANGE 1: M1.1a data source (node 8) ===
const node8 = adf.content[8];
if (node8 && node8.content) {
  for (let i = 0; i < node8.content.length; i++) {
    if (node8.content[i].text && node8.content[i].text.includes('survey or platform analytics')) {
      node8.content[i].text = node8.content[i].text.replace('survey or platform analytics', 'self-reported survey');
      console.log('CHANGE 1: Fixed M1.1a data source');
    }
  }
}

// === CHANGE 2: Add M1.2a section (insert before node 12 which is M1.2b) ===
const m12aNodes = [
  heading(3, "M1.2a: AI-Augmented Workflow Documentation"),
  paragraph([
    textNode("Metric:", [{ type: "strong" }]),
    textNode(" Number of documented AI-augmented workflow patterns for PE internal use")
  ]),
  paragraph([
    textNode("Definition:", [{ type: "strong" }]),
    textNode(" Count of documented patterns where AI augments PE team\u2019s internal workflows (AI as co-pilot with human in the loop). Examples: Operations Review prep using Claude, meeting preparation with AI assistance, data analysis with AI support.")
  ]),
  paragraph([
    textNode("Target:", [{ type: "strong" }]),
    textNode(" \u22655 documented patterns by Q2 2027")
  ]),
  paragraph([
    textNode("Owner:", [{ type: "strong" }]),
    textNode(" "),
    mention(VERA, "Vera Branco"),
    textNode(" ")
  ]),
  paragraph([
    textNode("Scope:", [{ type: "strong" }]),
    textNode(" Internal PE team workflows \u2014 how PE uses AI tools for their own work")
  ]),
  paragraph([
    textNode("Focus:", [{ type: "strong" }]),
    textNode(" PE team capability building and productivity gains")
  ]),
  paragraph([
    textNode("Process Gaps:", [{ type: "strong" }])
  ]),
  bulletList([
    [textNode("\u201CDocumented pattern\u201D definition", [{ type: "strong" }]), textNode(" \u2014 what qualifies? Template required? Minimum detail level? Format?")],
    [textNode("Documentation location", [{ type: "strong" }]), textNode(" \u2014 Confluence? Team wiki? Knowledge base?")],
    [textNode("Validation criteria", [{ type: "strong" }]), textNode(" \u2014 who validates a pattern is complete enough to count?")],
    [textNode("Prioritization approach", [{ type: "strong" }]), textNode(" \u2014 which workflows to document first?")],
    [textNode("Usefulness validation", [{ type: "strong" }]), textNode(" \u2014 how to ensure patterns are actually useful vs documentation for documentation\u2019s sake?")]
  ]),
  paragraph([
    textNode("Baseline:", [{ type: "strong" }]),
    textNode(" 0 documented patterns (Q2 2026)")
  ]),
  rule()
];

adf.content.splice(12, 0, ...m12aNodes);
const offset1 = m12aNodes.length;
console.log('CHANGE 2: Inserted M1.2a section (' + offset1 + ' nodes at index 12)');

// === CHANGE 3: M1.3a target fix ===
const m13aBulletIdx = 26 + offset1;
const m13aBullet = adf.content[m13aBulletIdx];
if (m13aBullet && m13aBullet.type === 'bulletList') {
  const secondItem = m13aBullet.content[1];
  if (secondItem) {
    const para = secondItem.content[0];
    if (para && para.content) {
      for (let i = 0; i < para.content.length; i++) {
        if (para.content[i].text && para.content[i].text.includes('Q2 2027')) {
          para.content[i].text = para.content[i].text.replace('Q2 2027', 'Q3 2026');
          console.log('CHANGE 3: Fixed M1.3a second bullet target to Q3 2026');
        }
      }
    }
  }
} else {
  console.log('WARNING: M1.3a bullet not found at index ' + m13aBulletIdx + ', type: ' + (m13aBullet ? m13aBullet.type : 'undefined'));
}

// === CHANGE 4: M3.4 owner mention ===
const m34OwnerIdx = 123 + offset1;
const m34Owner = adf.content[m34OwnerIdx];
if (m34Owner && m34Owner.content) {
  const hasPlainInes = m34Owner.content.some(c => c.text && c.text.includes('In\u00EAs Matos') && c.type === 'text' && !c.attrs);
  if (hasPlainInes) {
    adf.content[m34OwnerIdx] = paragraph([
      textNode("Owner:", [{ type: "strong" }]),
      textNode(" "),
      mention(INES, "In\u00EAs Matos"),
      textNode(" ")
    ], m34Owner.attrs.localId);
    console.log('CHANGE 4: Fixed M3.4 owner with proper mention');
  } else {
    console.log('WARNING: M3.4 owner node does not contain plain Ines text');
  }
}

// === CHANGE 5: M3.4d owner mention ===
const m34dOwnerIdx = 158 + offset1;
const m34dOwner = adf.content[m34dOwnerIdx];
if (m34dOwner && m34dOwner.content) {
  const hasPlainInes = m34dOwner.content.some(c => c.text && c.text.includes('In\u00EAs Matos') && c.type === 'text' && !c.attrs);
  if (hasPlainInes) {
    adf.content[m34dOwnerIdx] = paragraph([
      textNode("Owner:", [{ type: "strong" }]),
      textNode(" "),
      mention(INES, "In\u00EAs Matos"),
      textNode(" ")
    ], m34dOwner.attrs.localId);
    console.log('CHANGE 5: Fixed M3.4d owner with proper mention');
  } else {
    console.log('WARNING: M3.4d owner node does not contain plain Ines text');
  }
}

// === CHANGE 6: Add M1.2b process gaps ===
// Find the rule that ends M1.2b section (between M1.2b and M1.3a)
let m12bRuleIdx = -1;
for (let i = 12 + offset1; i < 12 + offset1 + 15; i++) {
  if (adf.content[i] && adf.content[i].type === 'rule') {
    m12bRuleIdx = i;
    break;
  }
}
if (m12bRuleIdx > 0) {
  const m12bGaps = [
    paragraph([textNode("Process Gaps:", [{ type: "strong" }])]),
    bulletList([
      [textNode("Baseline establishment approach", [{ type: "strong" }]), textNode(" \u2014 time tracking for specific workflows? Estimates? Historical data?")],
      [textNode("Which workflows to baseline", [{ type: "strong" }]), textNode(" \u2014 all workflows? Just top 5 from M1.2a?")],
      [textNode("Measurement accuracy", [{ type: "strong" }]), textNode(" \u2014 self-reported? Before/after comparison?")],
      [textNode("Individual variation", [{ type: "strong" }]), textNode(" \u2014 track individually? Average across team? Normalize?")],
      [textNode("Isolating AI impact", [{ type: "strong" }]), textNode(" \u2014 how to separate AI savings from other efficiency improvements?")]
    ])
  ];
  adf.content.splice(m12bRuleIdx, 0, ...m12bGaps);
  console.log('CHANGE 6: Added M1.2b process gaps (' + m12bGaps.length + ' nodes before index ' + m12bRuleIdx + ')');
}

// Save
const outputPath = 'C:/Users/vbr/.claude/projects/C--Users-vbr-Desktop-Veriski-Veriski/dd64aced-4ddb-441b-bfec-ebd3cedd88e4/tool-results/modified_adf.json';
fs.writeFileSync(outputPath, JSON.stringify(adf));
console.log('Saved modified ADF to', outputPath);
console.log('Total nodes:', adf.content.length);
