---
title: Processes crashes and other behaviors in Sentry machines
confluence_url: https://outsystemsrd.atlassian.net/wiki/spaces/RCP/pages/3483042714/Processes+crashes+and+other+behaviors+in+Sentry+machines
confluence_space: RCP
confluence_page_id: 3483042714
last_synced: 2026-04-09
owner: Process Engineering
---

# Processes crashes and other behaviors in Sentry machines

On the OutSystems PaaS the environment setup is slightly different than other installations since the machines are &ldquo;hardened&rdquo; with different configurations to make them more secure.

One of the main differences is that instead of no anti-virus (or Windows Defender)** there is Trend Micro installed**.

One behavior that could be seen on the environments is when some processes suddenly crash without leaving any trace behind.

In the case of the OutSystems Services, luckily there is and error from the Service Control Manager to at least track the exit moment:

The troubleshooting of this is really hard, because using usual tools like DebugDiag2 may not detect any process crash. Still it&rsquo;s probably a good idea to setup the DebugDiag2 and try to do it as the output log will may tell **a different cause or help confirm the suspicions**.

In the case that we were recently troubleshooting in the logs it appeared that everything was exiting without any error, appearing that the CompilerService was exiting normally and without any fatal exception:

  Thread exited. Exiting thread - System ID: 9332. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 4576. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 8212. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 2280. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 7376. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 2832. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 2012. Exit code - 0x00000000
  Thread exited. Exiting thread - System ID: 1780. Exit code - 0x00000000
  Process exited. Exit code - 0x00000000

To be able to see if there was any action from Trend Micro follow the steps:

- 
Open a console in administration mode

- 
Execute the command: `D:\trendmicro\ds_control.exe -d`

- 
Open an explorer window in `C:\ProgramData\Trend Micro\Deep Security Agent\diag\`

- 
Open the `ds_agent-NN.log` file in a file editor

- 
Check the files for evidences of an action taken by it. Example: