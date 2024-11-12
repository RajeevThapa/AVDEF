import os
import time
import subprocess
import yaml
import requests
from zapv2 import ZAPv2

def start_zap_daemon():
    zap_command = "zaproxy -daemon -port 8080 -config api.disablekey=true"
    
    try:
        # Start ZAP as a background process without waiting for stdout/stderr
        process = subprocess.Popen(zap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Waiting for ZAP to start...")
        time.sleep(20)
        
        zap_url = "http://localhost:8080"
        response = requests.get(zap_url)
        
        if response.status_code == 200:
            print("ZAP started successfully in daemon mode.")
        else:
            print(f"Failed to connect to ZAP daemon. Status code: {response.status_code}")
            process.kill()
            exit(1)
    
    except Exception as e:
        print(f"Error while starting ZAP daemon: {e}")
        exit(1)

def run_passive_scan():
    # Load configuration from YAML file
    zap_config_path = os.path.join(os.getenv('WORKSPACE', '.'), 'configs', 'zap_config.yaml')
    with open(zap_config_path) as config_file:
        config = yaml.safe_load(config_file)

    target_url = os.getenv('TARGET_URL', config["target_url"])  # Override from environment variable if set
    output_dir = os.getenv('OUTPUT_DIR', config["output_dir"])  # Override from environment variable if set

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    safe_target_url = target_url.replace('http://', '').replace('https://', '').replace('/', '_')
    output_file = os.path.join(output_dir, f"{safe_target_url}_zap_report.html")

    zap = ZAPv2()

    print(f"Starting passive scan on {target_url}...")

    try:
        zap.urlopen(target_url)
        time.sleep(2)

        print("Passive scan is in progress...")
        time.sleep(10)  # Wait for passive scan to complete

        print("ZAP passive scan completed.")

        # Save the scan results as an HTML report
        with open(output_file, 'w') as f:
            f.write(zap.core.htmlreport())

        print(f"ZAP passive scan results saved to {output_file}")
    except Exception as e:
        print(f"Error during passive scan: {e}")

if __name__ == "__main__":
    start_zap_daemon()
    run_passive_scan()
