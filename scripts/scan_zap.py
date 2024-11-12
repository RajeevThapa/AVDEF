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

if __name__ == "__main__":
    start_zap_daemon()
    run_passive_scan()
