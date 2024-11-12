pipeline {
    agent any

    environment {
        // Set environment variables for target URL and output directory
        TARGET_URL = 'http://testhtml5.vulnweb.com/'  // Provide the target URL here
        OUTPUT_DIR = '/var/lib/jenkins/workspace/zap_scans/zap_reports/'  // Provide the desired output directory here
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    credentialsId: 'c2a210b9-81da-4beb-ab7d-8c001b2fb92b', // Jenkins integration with GitHub
                    url: 'https://github.com/RajeevThapa/AVDEF'
            }
        }
        
        stage('Activate Virtual Environment') {
            steps {
                script {
                    // Activate the virtual environment from the existing venv folder using '.' (dot) instead of 'source'
                    echo 'Activating virtual environment...'
                    sh '. venv/bin/activate'  // Use dot instead of source for sh compatibility
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt using pip
                    echo 'Installing Python dependencies...'
                    sh 'pip install -r requirements.txt'  // Install dependencies (including zapv2)
                }
            }
        }

        stage('Run Nmap Scan') {
            steps {
                script {
                    // Run Nmap scan script (scan_nmap.py)
                    echo 'Running Nmap scan...'
                    sh 'python3 scripts/scan_nmap.py'
                }
            }
        }

        stage('Run Nikto Scan') {
            steps {
                script {
                    // Run Nikto scan script (scan_nikto.py)
                    echo 'Running Nikto scan...'
                    sh 'python3 scripts/scan_nikto.py'
                }
            }
        }

        stage('Run ZAP Scan') {
            steps {
                script {
                    // Run ZAP scan script (scan_zap.py)
                    echo 'Running ZAP scan...'
                    sh 'python3 scripts/scan_zap.py'
                }
            }
        }

        stage('Run Metasploit Exploit') {
            steps {
                script {
                    // Run Metasploit exploitation script (exploit_metasploit.py)
                    echo 'Running Metasploit exploit...'
                    sh 'python3 scripts/exploit_metasploit.py'
                }
            }
        }

        stage('Generate Reports') {
            steps {
                script {
                    // Generate summary report from scan results (report_generator.py)
                    echo 'Generating summary report...'
                    sh 'python3 scripts/report_generator.py'
                }
            }
        }

        stage('Send Notification') {
            steps {
                script {
                    // Send email notification with the summary report (notify.py)
                    echo 'Sending notification email...'
                    sh 'python3 scripts/notify.py'
                }
            }
        }
    }
}
