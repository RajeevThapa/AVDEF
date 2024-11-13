import os
import time
import subprocess
import yaml
import requests
from zapv2 import ZAPv2

def start_zap_daemon():
    zap_command = "zaproxy -daemon -port 8080 -host 0.0.0.0 -config api.disablekey=true"
    process = subprocess.Popen(zap_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    for attempt in range(5):
        try:
            time.sleep(5)
            if requests.get("http://localhost:8080").status_code == 200:
                print("ZAP started successfully.")
                return
        except requests.ConnectionError:
            continue
    process.kill()
    print("Failed to start ZAP.")
    exit(1)

def run_passive_scan():
    config_path = os.path.join(os.getenv('WORKSPACE', '.'), 'configs', 'zap_config.yaml')
    with open(config_path) as file:
        config = yaml.safe_load(file)
    
    target_url = os.getenv('TARGET_URL', config["target_url"])
    output_dir = os.getenv('OUTPUT_DIR', config["output_dir"])
    os.makedirs(output_dir, exist_ok=True)
    
    safe_target_url = target_url.replace('http://', '').replace('https://', '').replace('/', '_')
    output_file = os.path.join(output_dir, f"{safe_target_url}_zap_report.html")

    zap = ZAPv2()
    zap.urlopen(target_url)
    time.sleep(10)
    with open(output_file, 'w') as f:
        f.write(zap.core.htmlreport())
    print(f"ZAP passive scan saved to {output_file}")

if __name__ == "__main__":
    start_zap_daemon()
    run_passive_scan()
