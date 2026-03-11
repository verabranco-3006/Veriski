// Script to process all 40 RDINCs and generate PDFs
const rdincList = [
  'RDINC-73594', 'RDINC-73508', 'RDINC-73357', 'RDINC-73318', 'RDINC-73305',
  'RDINC-73079', 'RDINC-72484', 'RDINC-72433', 'RDINC-72257', 'RDINC-70580',
  'RDINC-70523', 'RDINC-69791', 'RDINC-69351', 'RDINC-69158', 'RDINC-69035',
  'RDINC-68931', 'RDINC-68902', 'RDINC-68886', 'RDINC-68790', 'RDINC-68682',
  'RDINC-68588', 'RDINC-68016', 'RDINC-67432', 'RDINC-67049', 'RDINC-67017',
  'RDINC-66959', 'RDINC-66775', 'RDINC-66627', 'RDINC-66235', 'RDINC-66210',
  'RDINC-66160', 'RDINC-65514', 'RDINC-65317', 'RDINC-65235', 'RDINC-64990',
  'RDINC-64745', 'RDINC-64453', 'RDINC-64382', 'RDINC-64148', 'RDINC-63913'
];

async function processRDINC(page, rdinc) {
  try {
    console.log(`Processing ${rdinc}...`);

    // Navigate to RDINC
    await page.goto(`https://outsystemsrd.atlassian.net/browse/${rdinc}`, {
      waitUntil: 'networkidle',
      timeout: 30000
    });

    // Wait for page to load
    await page.waitForTimeout(2000);

    // Collapse sidebar if not already collapsed
    try {
      const collapseButton = page.getByRole('button', { name: /Collapse sidebar/ });
      if (await collapseButton.isVisible()) {
        await collapseButton.click();
        await page.waitForTimeout(500);
      }
    } catch (e) {
      // Sidebar already collapsed
    }

    // Click "All" in Activity section
    try {
      const allButton = page.getByTestId('issue-activity-feed.ui.buttons.AllActivity');
      if (await allButton.isVisible()) {
        await allButton.click();
        await page.waitForTimeout(1000);
      }
    } catch (e) {
      console.log(`  Could not click All button for ${rdinc}`);
    }

    // Generate PDF
    await page.pdf({
      path: `${rdinc}.pdf`,
      format: 'A4',
      printBackground: true,
      scale: 0.7,
      margin: {
        top: '10mm',
        right: '10mm',
        bottom: '10mm',
        left: '10mm'
      }
    });

    console.log(`  ✓ ${rdinc} completed`);
    return { rdinc, status: 'success' };

  } catch (error) {
    console.log(`  ✗ ${rdinc} FAILED: ${error.message}`);
    return { rdinc, status: 'error', error: error.message };
  }
}

module.exports = { rdincList, processRDINC };
