import os
import time
import subprocess
import yaml
import requests
from zapv2 import ZAPv2

def start_zap_daemon():
    zap_command = "zaproxy -daemon -port 8081 -host 0.0.0.0 -config api.disablekey=true"
    
    try:
        process = subprocess.Popen(zap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Started ZAP daemon process with PID: ", process.pid)

        retries = 5
        for attempt in range(retries):
            print(f"Attempt {attempt + 1} to connect to ZAP...")
            time.sleep(5)  # Wait for ZAP to start
            zap_url = "http://localhost:8081"
            try:
                response = requests.get(zap_url)
                if response.status_code == 200:
                    print("ZAP started successfully in daemon mode.")
                    break
            except requests.ConnectionError as e:
                if attempt == retries - 1:
                    print("Failed to connect to ZAP daemon after multiple attempts.")
                    process.kill()
                    exit(1)
                else:
                    print(f"Error: {e}. Retrying...")
    except Exception as e:
        print(f"Error while starting ZAP daemon: {e}")
        exit(1)

def run_passive_scan():
    # Initialize the ZAP API client
    zap = ZAPv2(proxies={'http': 'http://localhost:8081', 'https': 'http://localhost:8081'})
    
    # Access the target URL to populate ZAP with data to scan
    target_url = os.environ.get('TARGET_URL', 'http://testhtml5.vulnweb.com/')
    print(f"Accessing target URL: {target_url} for passive scan.")
    zap.urlopen(target_url)
    time.sleep(2)  # Allow time for the page to load in ZAP
    
    # Start passive scan on the target
    print("Starting passive scan...")
    scan_id = zap.pscan.scan()
    
    # Monitor passive scan status
    while int(zap.pscan.records_to_scan) > 0:
        print(f"Records remaining in passive scan: {zap.pscan.records_to_scan}")
        time.sleep(5)

    print("Passive scan completed.")
    # Save the scan report
    report_path = os.path.join(os.environ.get('OUTPUT_DIR', '/tmp'), 'zap_passive_report.html')
    with open(report_path, 'w') as report_file:
        report_file.write(zap.core.htmlreport())
    print(f"Passive scan report saved to: {report_path}")

if __name__ == "__main__":
    start_zap_daemon()
    run_passive_scan()
