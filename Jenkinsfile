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

                    // Ensure the virtual environment is activated for subsequent steps
                    echo 'Virtual environment created.'
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing Python dependencies...'
                    // Activate the virtual environment and install dependencies
                    sh """
                        source ${VENV_DIR}/bin/activate  # Activate the virtual environment
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
                // sh 'python3 scripts/scan_nmap.py'  // Uncomment when you add the Nmap scan script
            }
        }

        stage('Run Nikto Scan') {
            steps {
                echo 'Running Nikto scan...'
                // sh 'python3 scripts/scan_nikto.py'  // Uncomment when you add the Nikto scan script
            }
        }

        stage('Run ZAP Scan') {
            steps {
                echo 'Running ZAP scan...'
                script {
                    // Activate venv and run ZAP scan script
                    sh """
                        source ${VENV_DIR}/bin/activate
                        python3 scripts/scan_zap.py  # Ensure this script exists and is executable
                    """
                }
            }
        }

        stage('Run Metasploit Exploit') {
            steps {
                echo 'Running Metasploit exploit...'
                // sh 'python3 scripts/scan_metasploit.py'  // Uncomment when you add the Metasploit exploit script
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Generating reports...'
                script {
                    // Ensure the virtual environment is activated before running the report generator
                    sh """
                        source ${VENV_DIR}/bin/activate
                        python3 scripts/report_generator.py  # Run the report generator script
                    """
                }
            }
        }

        stage('Send Notification') {
            steps {
                echo 'Sending notifications...'
                // Example: Send notification through Slack or Email
                sh 'python3 scans/notify.py'  // Ensure this script exists
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
