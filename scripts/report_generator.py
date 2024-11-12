import os
import glob
import html2text
from bs4 import BeautifulSoup

def convert_zap_html_to_md(zap_html_path):
    """Convert ZAP HTML report to Markdown format"""
    try:
        with open(zap_html_path, "r") as zap_report:
            html_content = zap_report.read()

        # Parse HTML and extract main content (adjust according to your needs)
        soup = BeautifulSoup(html_content, "html.parser")

        # Optionally extract only the relevant sections
        main_content = soup.find('div', {'class': 'main_content'})  # Example: adjust selector
        if main_content:
            html_content = str(main_content)

        # Use html2text to convert HTML to Markdown
        md_converter = html2text.HTML2Text()
        md_content = md_converter.handle(html_content)

        return md_content
    except Exception as e:
        print(f"Error converting ZAP HTML report to Markdown: {e}")
        return "Failed to convert ZAP report."

def generate_report():
    # Get workspace directory from environment or default to current directory
    workspace_dir = os.getenv('WORKSPACE', '.')

    # Define directories for different reports
    report_dir = os.path.join(workspace_dir, "scans", "reports")
    nmap_dir = os.path.join(workspace_dir, "scans", "nmap")
    zap_dir = os.path.join(workspace_dir, "scans", "zap")
    nikto_dir = os.path.join(workspace_dir, "scans", "nikto")

    # Ensure report directory exists
    os.makedirs(report_dir, exist_ok=True)

    # Find latest report in each directory
    nmap_report_path = glob.glob(os.path.join(nmap_dir, "*_nmap.txt"))[0] if glob.glob(os.path.join(nmap_dir, "*_nmap.txt")) else None
    zap_report_path = glob.glob(os.path.join(zap_dir, "*_zap_report.html"))[0] if glob.glob(os.path.join(zap_dir, "*_zap_report.html")) else None
    nikto_report_path = glob.glob(os.path.join(nikto_dir, "*_nikto.txt"))[0] if glob.glob(os.path.join(nikto_dir, "*_nikto.txt")) else None

    # Path for summary report
    summary_report_path = os.path.join(report_dir, "summary_report.md")

    try:
        with open(summary_report_path, "w") as report:
            report.write("# Vulnerability Scan Report\n\n")

            # Aggregate Nmap
            if nmap_report_path:
                with open(nmap_report_path, "r") as nmap_report:
                    report.write("## Nmap Scan Results\n")
                    report.write(nmap_report.read())
            else:
                report.write("## Nmap Scan Results\n")
                report.write("Nmap scan report not found.\n")

            # Aggregate ZAP
            if zap_report_path:
                zap_md_content = convert_zap_html_to_md(zap_report_path)
                report.write("## ZAP Scan Results\n")
                report.write(zap_md_content)
            else:
                report.write("## ZAP Scan Results\n")
                report.write("ZAP scan report not found.\n")

            # Aggregate Nikto
            if nikto_report_path:
                with open(nikto_report_path, "r") as nikto_report:
                    report.write("## Nikto Scan Results\n")
                    report.write(nikto_report.read())
            else:
                report.write("## Nikto Scan Results\n")
                report.write("Nikto scan report not found.\n")

        print(f"Report generated at {summary_report_path}")
    except Exception as e:
        print(f"Error generating the report: {e}")

if __name__ == "__main__":
    generate_report()
