vuln_auto_framework/
├── scans/
│   ├── nmap/
│   ├── nikto/
│   ├── openvas/
│   ├── zap/
│   └── reports/
├── scripts/
│   ├── scan_nmap.py
│   ├── scan_openvas.py
│   ├── scan_zap.py
│   └── scan_nikto.py
│   ├── exploit_metasploit.py
│   ├── report_generator.py
│   └── notify.py
├── configs/
│   ├── zap_config.yaml
│   ├── openvas_config.yaml
│   └── metasploit.rc
├── Jenkinsfile
└── README.md

# Project Workflow

## 1. Scan Targets: Using Nmap, OWASP ZAP and, Nikto to identify vulnerabilities.
## 2. Exploit Detected Vulnerabilities: Use Metasploit and other tools for automated exploitation.
## 3. Generate Reports: Aggregate results and format them into a report.
## 4. Notifications: Notify the team on scan completion and send reports.
## 5. Automate with Jenkins: Set up Jenkins to run the entire process on schedule or on-demand.

### Step 1: Set Up Configuration Files
- zap_config.yaml
- openvas_config.yaml (Not Using GVM to huge disc space it allocates around 10-20 gb)
- metasploit.rc

### Step 2: Write Vulnerability Detection Scripts
- scan_nmap.py
- scan_openvas.py (Not Using GVM to huge disc space it allocates around 10-20 gb)
- scan_zap.py
- scan_nikto.py

### Step 3: Exploitation Script with Metasploit
- exploit_metasploit.py

### Step 4: Report Generation Script
- report_generator.py

### Step 5: Notifications Script
- notify.py

### Step 6: Jenkinsfile for CI/CD Pipeline
- Jenkinsfile

#### Dependencies
- Zapproxy

zaproxy -daemon -port 8080 -config api.disablekey=true

- Taken Vulnerable test website from: http://www.vulnweb.com/
- scan_namp.py takes 459.70 seconds to scan http://testhtml5.vulnweb.com/
- scan_zap.py takes 30 seconds to passive scan and takes 1200 seconds approx for active scan http://testhtml5.vuln
- scan_nikto.py takes 387 seconds to scan http://testhtml5.vul

- exploit_metasploit.py: script successfully ran the dir_scanner module on testhtml5.vulnweb.com, targeting the /admin/ path, and completed without errors. The scan didn’t report any further results in this output, which implies that: No vulnerable directories or pages were found under /admin/ with the 404 status used as a filter, meaning pages or files under /admin/ may not be accessible or do not exist on the target. Scan Completion: The message “[*] Auxiliary module execution completed” confirms that the scan completed successfully, without interruptions.To perform a more comprehensive scan or identify vulnerabilities in other areas, Expand Directory Paths: Add other directories commonly found on web servers, such as /login/, /config/, /backup/, etc., to the PATH setting and re-run dir_scanner.