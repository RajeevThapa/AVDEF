pipeline {
    agent any

    environment {
        // Set environment variables for target URL and output directory
        TARGET_URL = 'http://testhtml5.vulnweb.com/'  // Provide the target URL here
        OUTPUT_DIR = '/var/lib/jenkins/workspace/zap_scans/zap_reports/'  // Provide the desired output directory here
        VIRTUAL_ENV = 'venv'  // Path to the virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git repository...'
                git branch: 'main', 
                    credentialsId: 'c2a210b9-81da-4beb-ab7d-8c001b2fb92b',  // Jenkins integration with GitHub
                    url: 'https://github.com/RajeevThapa/AVDEF'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    // Check if the virtual environment exists, and create if it doesn't
                    if (!fileExists("${VIRTUAL_ENV}/bin/activate")) {
                        echo 'Creating virtual environment...'
                        sh 'python3 -m venv venv'  // Create virtual environment
                    } else {
                        echo 'Virtual environment already exists.'
                    }
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python dependencies...'
                    // Activate the virtual environment and install dependencies
                    sh """
                        . venv/bin/activate  # Activate the virtual environment
                        pip install --upgrade pip  # Ensure pip is the latest version
                        pip install --upgrade urllib3 six  # Upgrade urllib3 and six
                        pip install -r requirements.txt  # Install dependencies from requirements.txt
                    """
                }
            }
        }


        stage('Run Nmap Scan') {
            steps {
                echo 'Running Nmap scan...'
                // sh 'python3 scripts/scan_nmap.py'
            }
        }

        stage('Run Nikto Scan') {
            steps {
                echo 'Running Nikto scan...'
                // sh 'python3 scripts/scan_nikto.py'
            }
        }

        stage('Run ZAP Scan') {
            steps {
                echo 'Running ZAP scan...'
                script {
                    // Run the ZAP scan script after activating the virtual environment
                    sh """
                        . venv/bin/activate  # Activate the virtual environment
                        python3 scripts/scan_zap.py  # Run ZAP scan script
                    """
                }
            }
        }

        stage('Run Metasploit Exploit') {
            steps {
                echo 'Running Metasploit exploit...'
                // sh 'python3 scripts/scan_metasploit.py'
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Generating reports...'
                // Assuming generate_reports.py generates the necessary reports
                sh 'python3 scripts/report_generator.py'
            }
        }

        stage('Send Notification') {
            steps {
                echo 'Sending notifications...'
                // Example: Send notification through Slack or Email
                sh 'python3 scans/notify.py'
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
