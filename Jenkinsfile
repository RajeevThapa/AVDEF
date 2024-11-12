pipeline {
    agent any

    environment {
        // Set environment variables for target URL and output directory
        TARGET_URL = 'http://testhtml5.vulnweb.com/'  // Provide the target URL here
        OUTPUT_DIR = '/var/lib/jenkins/workspace/zap_scans/zap_reports/'  // Provide the desired output directory here
        VENV_DIR = 'venv'  // Path to the virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git repository...'
                checkout scm
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    // Remove any existing virtual environment (if exists)
                    sh "rm -rf ${VENV_DIR}"

                    // Create a new virtual environment
                    sh "python3 -m venv ${VENV_DIR}"

                    // Ensure the virtual environment is created successfully
                    echo 'Virtual environment created.'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python dependencies...'
                    // Activate the virtual environment using bash
                    sh """
                        bash -c 'source ${VENV_DIR}/bin/activate && pip install --upgrade pip && pip install --upgrade urllib3 six && pip install -r requirements.txt'
                    """
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                echo 'Running Nmap scan...'
                sh 'python3 scripts/scan_nmap.py'
            }
        }

        stage('Run Nikto Scan') {
            steps {
                echo 'Running Nikto scan...'
                sh 'python3 scripts/scan_nikto.py'
            }
        }

        stage('Run ZAP Scan') {
            steps {
                echo 'Running ZAP scan...'
                script {
                    // Activate venv and run ZAP scan script using bash
                    sh """
                        bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/scan_zap.py'
                    """
                }
            }
        }

        stage('Run Metasploit Exploit') {
            steps {
                echo 'Running Metasploit exploit...'
                sh 'python3 scripts/exploit_metasploit.py'
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Generating reports...'
                script {
                    // Ensure the virtual environment is activated before running the report generator
                    sh """
                        bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/report_generator.py'
                    """
                }
            }
        }

        stage('Send Notification') {
            steps {
                echo 'Sending notifications...'
                // Example: Send notification through Slack or Email
                // sh 'python3 scans/notify.py'
            }
        }

        stage('Commit and Push Scan Results') {
            steps {
                script {
                // Sanitize the TARGET_URL for use in file paths
                def sanitizedUrl = TARGET_URL.replaceAll('https?://', '').replaceAll('/', '_')
                
                // Define paths for the Git repository folder structure
                def zapReportPath = "${env.WORKSPACE}/scans/zap/${sanitizedUrl}_zap_report.html"
                def niktoReportPath = "${env.WORKSPACE}/scans/nikto/${sanitizedUrl}_nikto.txt"
                def nmapReportPath = "${env.WORKSPACE}/scans/nmap/${sanitizedUrl}_nmap.txt"
                def summaryReportPath = "${env.WORKSPACE}/scans/reports/summary_report.md"
                
                // Create directories if they don't exist
                sh "mkdir -p ${env.WORKSPACE}/scans/zap ${env.WORKSPACE}/scans/nikto ${env.WORKSPACE}/scans/nmap ${env.WORKSPACE}/scans/reports"
                
                // Copy the generated reports to the workspace
                // sh "cp /var/lib/jenkins/workspace/zap_scans/zap_reports/${sanitizedUrl}_zap_report.html ${zapReportPath}"
                // sh "cp /root/.jenkins/workspace/AVDEF/scans/nikto/${sanitizedUrl}_nikto.txt ${niktoReportPath}"
                // sh "cp /root/.jenkins/workspace/AVDEF/scans/nmap/${sanitizedUrl}_nmap.txt ${nmapReportPath}"
                // sh "cp /root/.jenkins/workspace/AVDEF/scans/reports/summary_report.md ${summaryReportPath}"
                sh "cp /var/lib/jenkins/workspace/zap_scans/zap_reports/${sanitizedUrl}_zap_report.html ${zapReportPath}"
                sh "cp ${env.WORKSPACE}/scans/nikto/${sanitizedUrl}_nikto.txt ${niktoReportPath}"
                sh "cp ${env.WORKSPACE}/scans/nmap/${sanitizedUrl}_nmap.txt ${nmapReportPath}"
                sh "cp ${env.WORKSPACE}/scans/reports/summary_report.md ${summaryReportPath}"

                // Commit and push the results
                sshagent(credentials: ['c2a210b9-81da-4beb-ab7d-8c001b2fb92b']) {
                    sh 'git add scans/zap scans/nikto scans/nmap scans/reports'
                    sh 'git commit -m "Add scan reports for ZAP, Nikto, Nmap, and summary"'
                    sh 'git push origin main'
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Any cleanup actions go here (e.g., removing temporary files, stopping containers)
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
