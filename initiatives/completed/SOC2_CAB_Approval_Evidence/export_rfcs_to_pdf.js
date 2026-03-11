// Script to export Normal RFCs to PDF for SOC2 Audit
const rfcList = [
  'RFC-2704', 'RFC-2713', 'RFC-2761', 'RFC-2839', 'RFC-2901', 'RFC-2986',
  'RFC-2993', 'RFC-3134', 'RFC-3136', 'RFC-3208', 'RFC-3437', 'RFC-3443',
  'RFC-3449', 'RFC-3465', 'RFC-3517', 'RFC-3562', 'RFC-3639', 'RFC-3640',
  'RFC-3659', 'RFC-3691', 'RFC-3922', 'RFC-4186', 'RFC-4213', 'RFC-4332'
];

async function exportRFCsToPDF(page) {
  const outputDir = 'SOC2_CAB_Approval_Evidence';
  let successCount = 0;
  let failCount = 0;

  for (const rfc of rfcList) {
    try {
      console.log(`Exporting ${rfc}...`);
      await page.goto(`https://outsystemsrd.atlassian.net/browse/${rfc}`, {
        waitUntil: 'networkidle'
      });

      // Wait for page to fully load
      await page.waitForTimeout(3000);

      await page.pdf({
        path: `${outputDir}/${rfc}.pdf`,
        format: 'A4',
        printBackground: true,
        margin: {
          top: '20px',
          right: '20px',
          bottom: '20px',
          left: '20px'
        }
      });

      successCount++;
      console.log(`✓ ${rfc} exported successfully`);
    } catch (error) {
      failCount++;
      console.error(`✗ Failed to export ${rfc}: ${error.message}`);
    }
  }

  return { successCount, failCount, total: rfcList.length };
}

// Export the function
exportRFCsToPDF;
