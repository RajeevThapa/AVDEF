import os
import glob
import html2text
from bs4 import BeautifulSoup

def convert_zap_html_to_md(zap_html_path):
    """Convert ZAP HTML report to Markdown format"""
    with open(zap_html_path, "r") as zap_report:
        html_content = zap_report.read()

    # Use BeautifulSoup to parse HTML and extract relevant sections
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Use html2text to convert HTML to Markdown
    md_converter = html2text.HTML2Text()
    md_content = md_converter.handle(html_content)
    
    # Return the converted markdown
    return md_content

def generate_report():
    # Get the Jenkins workspace directory from the environment variable, default to current directory if not found
    workspace_dir = os.getenv('WORKSPACE', '.')

    # Define the directories where the reports are stored, relative to the Jenkins workspace
    report_dir = os.path.join(workspace_dir, "scans", "reports")
    nmap_dir = os.path.join(workspace_dir, "scans", "nmap")
    zap_dir = os.path.join(workspace_dir, "scans", "zap")
    nikto_dir = os.path.join(workspace_dir, "scans", "nikto")

    # Ensure the report directory exists
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Find the latest report in each directory using glob
    nmap_report_path = glob.glob(os.path.join(nmap_dir, "*_nmap.txt"))  # Matches all nmap report files
    zap_report_path = glob.glob(os.path.join(zap_dir, "*_zap_report.html"))  # Matches all zap report files
    nikto_report_path = glob.glob(os.path.join(nikto_dir, "*_nikto.txt"))  # Matches all nikto report files

    # If no report is found, set to None
    nmap_report_path = nmap_report_path[0] if nmap_report_path else None
    zap_report_path = zap_report_path[0] if zap_report_path else None
    nikto_report_path = nikto_report_path[0] if nikto_report_path else None

    # Path for the summary report in the reports directory
    summary_report_path = os.path.join(report_dir, "summary_report.md")

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

if __name__ == "__main__":
    generate_report()

# import os
# import glob
# import html2text
# from bs4 import BeautifulSoup

# def convert_zap_html_to_md(zap_html_path):
#     """Convert ZAP HTML report to Markdown format"""
#     with open(zap_html_path, "r") as zap_report:
#         html_content = zap_report.read()

#     # Use BeautifulSoup to parse HTML and extract relevant sections
#     soup = BeautifulSoup(html_content, "html.parser")
    
#     # Use html2text to convert HTML to Markdown
#     md_converter = html2text.HTML2Text()
#     md_content = md_converter.handle(html_content)
    
#     # Return the converted markdown
#     return md_content

# def generate_report():
#     # Define the directories where the reports are stored
#     report_dir = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/reports/"
#     nmap_dir = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/nmap/"
#     zap_dir = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/zap/"
#     nikto_dir = "/home/rajeev/User_rajeev/AAU/AVDEF/scans/nikto/"

#     # Find the latest report in each directory using glob
#     nmap_report_path = glob.glob(os.path.join(nmap_dir, "*_nmap.txt"))  # Matches all nmap report files
#     zap_report_path = glob.glob(os.path.join(zap_dir, "*_zap_report.html"))  # Matches all zap report files
#     nikto_report_path = glob.glob(os.path.join(nikto_dir, "*_nikto.txt"))  # Matches all nikto report files

#     # If no report is found, set to None
#     nmap_report_path = nmap_report_path[0] if nmap_report_path else None
#     zap_report_path = zap_report_path[0] if zap_report_path else None
#     nikto_report_path = nikto_report_path[0] if nikto_report_path else None

#     with open(f"{report_dir}summary_report.md", "w") as report:
#         report.write("# Vulnerability Scan Report\n\n")

#         # Aggregate Nmap
#         if nmap_report_path:
#             with open(nmap_report_path, "r") as nmap_report:
#                 report.write("## Nmap Scan Results\n")
#                 report.write(nmap_report.read())
#         else:
#             report.write("## Nmap Scan Results\n")
#             report.write("Nmap scan report not found.\n")

#         # Aggregate ZAP
#         if zap_report_path:
#             zap_md_content = convert_zap_html_to_md(zap_report_path)
#             report.write("## ZAP Scan Results\n")
#             report.write(zap_md_content)
#         else:
#             report.write("## ZAP Scan Results\n")
#             report.write("ZAP scan report not found.\n")

#         # Aggregate Nikto
#         if nikto_report_path:
#             with open(nikto_report_path, "r") as nikto_report:
#                 report.write("## Nikto Scan Results\n")
#                 report.write(nikto_report.read())
#         else:
#             report.write("## Nikto Scan Results\n")
#             report.write("Nikto scan report not found.\n")

#     print(f"Report generated at {report_dir}summary_report.md")

# if __name__ == "__main__":
#     generate_report()
