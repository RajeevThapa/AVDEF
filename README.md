# Automated Vulnerability Detection and Exploitation Framework (VDEF)

## Overview
AVDEF is a framework designed to automate the process of vulnerability detection, exploitation, and reporting. Tools like Nmap, Nikto, and OWASP ZAP for vulnerability scans, and Metasploit for exploitation, AVDEF automates each step, from scanning to notifying the security team(for now only sample SMTP has been setup) with detailed reports. For the non-automation part we have another repo which is modfied to work manually. Link: https://github.com/RajeevThapa/VDEF.

## Project Structure

```
Automated Vulnerability Detection and Exploitation Framework/
├── scans/                                                  # Stores scan outputs for various tools
│   ├── nmap/
│   ├── nikto/
│   ├── zap/
│   └── reports/
├── scripts/                                                # Contains Python scripts for scanning, exploitation, and reporting
│   ├── scan_nmap.py
│   ├── scan_zap.py
│   └── scan_nikto.py
│   ├── exploit_metasploit.py
│   ├── report_generator.py
│   └── notify.py
├── configs/                                                # Configuration files for ZAP, OpenVAS, and Metasploit
│   ├── zap_config.yaml
│   └── metasploit.rc
├── Jenkinsfile                                             # CI/CD pipeline for automating the workflow
└── README.md
```

## Workflow

### Step 1: Configure Scans
Define scan parameters in the configuration files:
- **zap_config.yaml**: Configuration for OWASP ZAP.
- **metasploit.rc**: Commands for Metasploit.

### Step 2: Run Vulnerability Detection Scripts
Execute scripts to scan for vulnerabilities:
- **scan_nmap.py**: Runs Nmap scans and saves results.
- **scan_zap.py**: Runs OWASP ZAP in passive/active mode based on configuration.
- **scan_nikto.py**: Runs Nikto scan for web vulnerabilities.

### Step 3: Exploit Detected Vulnerabilities
Using **exploit_metasploit.py**, automate Metasploit to exploit known vulnerabilities.

### Step 4: Generate Reports
The **report_generator.py** script aggregates and formats scan results into a markdown report.

### Step 5: Send Notifications
After report generation, **notify.py** sends the summary to the team via email.

### Step 6: Automate with Jenkins
Use **Jenkinsfile** to set up a CI/CD pipeline for automating the entire workflow on schedule or on demand.

## Prerequisites
- Python 3.6+
- Install dependencies: `pip install -r requirements.txt`
- Vulnerable test website used for demonstration: [http://www.vulnweb.com](http://www.vulnweb.com)

## Script Descriptions

### scan_nmap.py
Performs a vulnerability scan using Nmap. Saves the scan results in the `scans/nmap/` directory.
![Screenshot from 2024-11-12 18-01-36](https://github.com/user-attachments/assets/5c4beb60-c065-496a-9fb7-ba84c29c6791)

### scan_zap.py
- Starts OWASP ZAP in daemon mode.
- Passively or actively scans the target, as configured.
- Saves results to `scans/zap/`.
![Screenshot from 2024-11-12 18-02-08](https://github.com/user-attachments/assets/2b474ba5-57ea-463c-8635-2e3377a9ff49)

### scan_nikto.py
Executes Nikto for scanning web servers and identifying potential issues. Results are saved in `scans/nikto/`.
![Screenshot from 2024-11-12 18-01-52](https://github.com/user-attachments/assets/69225328-c20b-42af-87fb-8a9ef137ec1e)

### exploit_metasploit.py
Runs Metasploit with pre-defined commands in `metasploit.rc` to exploit vulnerabilities on the target.
![Screenshot from 2024-11-12 18-03-19](https://github.com/user-attachments/assets/b2c29a9c-7e7a-468e-aca3-bd9254f05f83)

### report_generator.py
Converts scan results from Nmap, ZAP, and Nikto into a summarized markdown report, saved in `scans/reports/summary_report.md`.

### notify.py
Sends the vulnerability scan report via email to the security team. Below is the email sent from the Jenkins pipeline to the mailing server.
![image](https://github.com/user-attachments/assets/7263bc00-3aa4-431e-8c25-de23b7f0786b)


## Jenkins CI/CD Pipeline
Automate the end-to-end process with Jenkins by executing the steps in `Jenkinsfile`.
![image](https://github.com/user-attachments/assets/db3b5420-84b9-40f2-b5d4-528a91ac6bf3)

## Sample Runtime Statistics
- **scan_nmap.py**: Approx. 460 seconds for `http://testhtml5.vulnweb.com`.
- **scan_zap.py**: ~30 seconds (passive) and 1200 seconds (active) for `http://testhtml5.vulnweb.com`.
- **scan_nikto.py**: Approx. 387 seconds for `http://testhtml5.vulnweb.com`.
