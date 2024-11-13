import os
import subprocess

def run_nikto_scan(target_ip):
    target_ip = target_ip.replace('http://', '').replace('https://', '').rstrip('/')
    safe_target_ip = target_ip.replace(':', '_').replace('/', '_')
    output_dir = os.getenv('NIKTO_OUTPUT_DIR', './scans/nikto/')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{safe_target_ip}_nikto.txt")

    try:
        command = f"nikto -h {target_ip} -Tuning 1 -output {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Nikto scan completed. Results saved in {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Nikto scan: {e}")

if __name__ == "__main__":
    target_ip = os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com')
    run_nikto_scan(target_ip)
