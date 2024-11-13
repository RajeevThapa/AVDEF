import os
import subprocess

def run_nikto_scan():
    target_url = os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com')
    safe_target_url = target_url.replace('http://', '').replace('https://', '').replace('/', '_')
    output_file = os.path.join(os.getenv('WORKSPACE', '.'), "scans", "nikto", f"{safe_target_url}_nikto.txt")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    command = f"nikto -h {target_url} -Tuning 1 -output {output_file}"
    subprocess.run(command, shell=True, check=True)
    print(f"Nikto scan saved to {output_file}")

if __name__ == "__main__":
    run_nikto_scan()
