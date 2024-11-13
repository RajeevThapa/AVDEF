import os
import glob
import html2text
from bs4 import BeautifulSoup

def convert_zap_html_to_md(zap_html_path):
    with open(zap_html_path, "r") as zap_report:
        html_content = zap_report.read()
    soup = BeautifulSoup(html_content, "html.parser")
    md_content = html2text.HTML2Text().handle(str(soup))
    return md_content

def generate_report():
    workspace_dir = os.getenv('WORKSPACE', '.')
    report_dir = os.path.join(workspace_dir, "scans", "reports")
    os.makedirs(report_dir, exist_ok=True)
    summary_report_path = os.path.join(report_dir, "summary_report.md")

    with open(summary_report_path, "w") as report:
        report.write("# Vulnerability Scan Report\n\n")
        
        # Aggregate Nmap results
        nmap_report_path = glob.glob(os.path.join(workspace_dir, "scans", "nmap", "*_nmap.txt"))
        if nmap_report_path:
            with open(nmap_report_path[0], "r") as nmap_report:
                report.write("## Nmap Scan Results\n")
                report.write(nmap_report.read())
        
        # Aggregate ZAP results
        zap_report_path = glob.glob(os.path.join(workspace_dir, "scans", "zap", "*_zap_report.html"))
        if zap_report_path:
            zap_md_content = convert_zap_html_to_md(zap_report_path[0])
            report.write("## ZAP Scan Results\n")
            report.write(zap_md_content)
        
        # Aggregate Nikto results
        nikto_report_path = glob.glob(os.path.join(workspace_dir, "scans", "nikto", "*_nikto.txt"))
        if nikto_report_path:
            with open(nikto_report_path[0], "r") as nikto_report:
                report.write("## Nikto Scan Results\n")
                report.write(nikto_report.read())

    print(f"Report generated at {summary_report_path}")

if __name__ == "__main__":
    generate_report()
