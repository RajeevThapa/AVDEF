import os

def run_nmap(target):
    # Remove 'http://' or 'https://' prefixes, if present, and trailing slash
    target = target.replace('http://', '').replace('https://', '').rstrip('/')

    # Create a safe filename by replacing characters that are invalid in filenames
    safe_target = target.replace(':', '_').replace('/', '_')

    # Get the workspace environment variable (Jenkins workspace)
    output_file = os.path.join(os.getenv('WORKSPACE', '.'), "scans", "nmap", f"{safe_target}_nmap.txt")

    # Run the Nmap scan using os.system
    os.system(f"nmap -sV --script vuln {target} -oN {output_file}")
    print(f"Nmap scan completed. Results saved in {output_file}")

if __name__ == "__main__":
    # Read the target URL from the environment variable (passed by Jenkins pipeline)
    target = os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com')  # Default if not provided
    run_nmap(target)
