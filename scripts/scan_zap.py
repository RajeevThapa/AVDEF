import os
import time
import subprocess
import yaml
import requests
from zapv2 import ZAPv2

def start_zap_daemon():
    zap_command = "zaproxy -daemon -port 8080 -config api.disablekey=true"
    try:
        process = subprocess.Popen(zap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Waiting for ZAP to start...")
        time.sleep(20)  # Adjust timing as needed
        zap_url = "http://localhost:8080"
        response = requests.get(zap_url)
        
        if response.status_code == 200:
            print("ZAP started successfully in daemon mode.")
        else:
            print("Failed to connect to ZAP daemon.")
            process.kill()
            exit(1)
    except Exception as e:
        print(f"Error starting ZAP daemon: {e}")
        exit(1)

def run_passive_scan():
    config_path = os.getenv('ZAP_CONFIG_PATH', './configs/zap_config.yaml')
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)
    target_url = os.getenv('TARGET_URL', config["target_url"])
    output_dir = os.getenv('ZAP_OUTPUT_DIR', config["output_dir"])

    os.makedirs(output_dir, exist_ok=True)
    safe_target_url = target_url.replace('http://', '').replace('https://', '').replace('/', '_')
    output_file = os.path.join(output_dir, f"{safe_target_url}_zap_report.html")
    zap = ZAPv2()
    print(f"Starting passive scan on {target_url}...")

    try:
        zap.urlopen(target_url)
        time.sleep(2)
        print("Passive scan is in progress...")
        time.sleep(10)
        print("ZAP passive scan completed.")

        with open(output_file, 'w') as f:
            f.write(zap.core.htmlreport())
        print(f"ZAP passive scan results saved to {output_file}")
    except Exception as e:
        print(f"Error during passive scan: {e}")

if __name__ == "__main__":
    start_zap_daemon()
    run_passive_scan()
