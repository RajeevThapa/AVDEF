pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'  // Path to the virtual environment
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    credentialsId: 'c2a210b9-81da-4beb-ab7d-8c001b2fb92b', // Jenkins integration with GitHub
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
                        . ${VIRTUAL_ENV}/bin/activate
                        pip install --upgrade pip  // Ensure pip is the latest version
                        pip install -r requirements.txt  // Install dependencies from requirements.txt
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
                sh 'python3 scripts/scan_zap.py'
            }
        }

        stage('Run Metasploit Exploit') {
            steps {
                echo 'Running Metasploit exploit...'
                sh 'python3 scripts/scan_metasploit.py'
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Generating reports...'
                sh 'python3 generate_reports.py'
            }
        }

        stage('Send Notification') {
            steps {
                echo 'Sending notifications...'
                // Example: Send notification through Slack or Email
                sh 'python3 send_notification.py'
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
