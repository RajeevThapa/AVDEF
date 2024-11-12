pipeline {
    agent any

    environment {
        // Set environment variables for target URL and output directory
        TARGET_URL = 'http://testhtml5.vulnweb.com/'  // Provide the target URL here
        OUTPUT_DIR = '/var/lib/jenkins/workspace/AVDEF/scans'  // Unified output directory for all scans
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
                sh 'python3 scripts/scan_nmap.py --output-dir ${OUTPUT_DIR}/nmap'
            }
        }

        stage('Run Nikto Scan') {
            steps {
                echo 'Running Nikto scan...'
                sh 'python3 scripts/scan_nikto.py --output-dir ${OUTPUT_DIR}/nikto'
            }
        }

        stage('Run ZAP Scan') {
            steps {
                echo 'Running ZAP scan...'
                script {
                    // Activate venv and run ZAP scan script using bash
                    sh """
                        bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/scan_zap.py --output-dir ${OUTPUT_DIR}/zap'
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
                        bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/report_generator.py --output-dir ${OUTPUT_DIR}/reports'
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
                    def sanitizedUrl = TARGET_URL.replaceAll('https?://', '').replaceAll('/', '_')
                    
                    // Define report paths
                    def zapReportPath = "${OUTPUT_DIR}/zap/${sanitizedUrl}_zap_report.html"
                    def niktoReportPath = "${OUTPUT_DIR}/nikto/${sanitizedUrl}_nikto.txt"
                    def nmapReportPath = "${OUTPUT_DIR}/nmap/${sanitizedUrl}_nmap.txt"
                    def summaryReportPath = "${OUTPUT_DIR}/reports/summary_report.md"
                    
                    // Copy reports to workspace
                    sh "mkdir -p ${env.WORKSPACE}/scans/zap ${env.WORKSPACE}/scans/nikto ${env.WORKSPACE}/scans/nmap ${env.WORKSPACE}/scans/reports"
                    sh "cp ${zapReportPath} ${env.WORKSPACE}/scans/zap/${sanitizedUrl}_zap_report.html"
                    sh "cp ${niktoReportPath} ${env.WORKSPACE}/scans/nikto/${sanitizedUrl}_nikto.txt"
                    sh "cp ${nmapReportPath} ${env.WORKSPACE}/scans/nmap/${sanitizedUrl}_nmap.txt"
                    sh "cp ${summaryReportPath} ${env.WORKSPACE}/scans/reports/summary_report.md"

                    // Commit and push
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
