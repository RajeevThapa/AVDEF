pipeline {
    agent any
    environment {
        TARGET_URL = "http://testhtml5.vulnweb.com"  // Change as needed
        ZAP_CONFIG_PATH = "./configs/zap_config.yaml"
        NMAP_OUTPUT_DIR = "./scans/nmap/"
        NIKTO_OUTPUT_DIR = "./scans/nikto/"
        ZAP_OUTPUT_DIR = "./scans/zap/"
        VENV_DIR = 'venv'  // Path to the virtual environment
    }
    stages {
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
        stage('Run ZAP Scan') {
            steps {
                script {
                    sh "bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/scan_zap.py'"
                }
            }
        }
        stage('Run Nmap Scan') {
            steps {
                script {
                    sh "bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/scan_nmap.py'"
                }
            }
        }
        stage('Run Nikto Scan') {
            steps {
                script {
                    sh "bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/scan_nikto.py'"
                }
            }
        }
        stage('Generate Report') {
            steps {
                script {
                    sh "bash -c 'source ${VENV_DIR}/bin/activate && python3 scripts/report_generator.py'"
                }
            }
        }
        stage('Send Notification') {
            steps {
                script {
                    echo "sending.."
                    // sh "python3 scripts/notify.py"
                }
            }
        }
        stage('Push Artifacts to GitHub') {
            steps {
                script {
                    // Use SSH credentials to push to GitHub
                    sshagent(credentials: ['c2a210b9-81da-4beb-ab7d-8c001b2fb92b']) {
                        sh 'git add scans/*'
                        sh 'git commit -m "Updated scan results and reports"'
                        sh 'git push -u origin path-a'
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'scans/**/*', allowEmptyArchive: true
            echo "All scan stages completed, and artifacts archived."
        }
    }
}
