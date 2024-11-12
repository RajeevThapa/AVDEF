import os
import subprocess

def run_nikto_scan():
    # Read the target URL from the environment variable (passed by Jenkins pipeline)
    target_url = os.getenv('TARGET_URL', 'http://testhtml5.vulnweb.com')  # Default if not provided
    
    # Remove 'http://' or 'https://' prefixes and trailing slash, if present
    target_url = target_url.replace('http://', '').replace('https://', '').rstrip('/')

    # Create a safe filename by replacing characters that are invalid in filenames
    safe_target_url = target_url.replace(':', '_').replace('/', '_')

    # Construct the output file path relative to Jenkins workspace
    output_file = os.path.join(os.getenv('WORKSPACE', '.'), "scans", "nikto", f"{safe_target_url}_nikto.txt")

    try:
        # Construct the command to run Nikto
        command = f"nikto -h {target_url} -Tuning 1 -output {output_file}"

        # Run the command and capture the output (if any)
        subprocess.run(command, shell=True, check=True)
        
        print(f"Nikto scan completed. Results saved in {output_file}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running Nikto scan: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_nikto_scan()
