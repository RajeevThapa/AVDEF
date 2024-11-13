import os

def run_nmap(target):
    target = target.replace('http://', '').replace('https://', '').rstrip('/')
    safe_target = target.replace(':', '_').replace('/', '_')
    output_dir = os.getenv('NMAP_OUTPUT_DIR', './scans/nmap/')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{safe_target}_nmap.txt")
    
    os.system(f"nmap -sV --script vuln {target} -oN {output_file}")
    print(f"Nmap scan completed. Results saved in {output_file}")

if __name__ == "__main__":
    target = os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com')
    run_nmap(target)
