import os

def run_nmap(target):
    target = target.replace('http://', '').replace('https://', '').rstrip('/')
    safe_target = target.replace(':', '_').replace('/', '_')
    output_file = os.path.join(os.getenv('WORKSPACE', '.'), "scans", "nmap", f"{safe_target}_nmap.txt")
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    os.system(f"nmap -sV --script vuln {target} -oN {output_file}")
    print(f"Nmap scan saved to {output_file}")

if __name__ == "__main__":
    run_nmap(os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com'))
