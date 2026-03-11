// Export RFC tickets to PDF for SOC2 CAB Approval Evidence
// Run with: node export_rfcs_script.js

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const rfcList = [
  'RFC-2704', 'RFC-2713', 'RFC-2761', 'RFC-2839', 'RFC-2901', 'RFC-2986',
  'RFC-2993', 'RFC-3134', 'RFC-3136', 'RFC-3208', 'RFC-3437', 'RFC-3443',
  'RFC-3449', 'RFC-3465', 'RFC-3517', 'RFC-3562', 'RFC-3639', 'RFC-3640',
  'RFC-3659', 'RFC-3691', 'RFC-3922', 'RFC-4186', 'RFC-4213', 'RFC-4332'
];

async function exportRFCs() {
  const outputDir = path.join(__dirname, 'SOC2_CAB_Approval_Evidence');

  // Ensure output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext();
  const page = await context.newPage();

  let successCount = 0;
  let failCount = 0;
  const results = [];

  for (const rfc of rfcList) {
    try {
      console.log(`Processing ${rfc}...`);

      await page.goto(`https://outsystemsrd.atlassian.net/browse/${rfc}`, {
        waitUntil: 'networkidle',
        timeout: 60000
      });

      // Wait for the CAB Review tab to be available
      await page.waitForTimeout(3000);

      // Click on CAB Review tab to ensure approval fields are visible
      const cabTab = page.locator('tab:has-text("CAB Review")');
      if (await cabTab.isVisible()) {
        await cabTab.click();
        await page.waitForTimeout(1000);
      }

      // Export to PDF using browser print function
      const pdfPath = path.join(outputDir, `${rfc}.pdf`);
      await page.pdf({
        path: pdfPath,
        format: 'A4',
        printBackground: true,
        margin: {
          top: '15mm',
          right: '15mm',
          bottom: '15mm',
          left: '15mm'
        },
        scale: 0.9
      });

      successCount++;
      results.push(`✓ ${rfc} exported successfully`);
      console.log(`✓ ${rfc} exported`);

    } catch (error) {
      failCount++;
      results.push(`✗ ${rfc} failed: ${error.message}`);
      console.error(`✗ Failed to export ${rfc}:`, error.message);
    }
  }

  await browser.close();

  console.log('\n=== Export Summary ===');
  console.log(`Total: ${rfcList.length}`);
  console.log(`Success: ${successCount}`);
  console.log(`Failed: ${failCount}`);
  console.log(`\nPDFs saved to: ${outputDir}`);

  return results;
}

exportRFCs().catch(console.error);
