pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                git url: 'https://github.com/sam2005-git/my-python-app.git' 
            }
        }
        stage('Setup Environment') {
            steps {
                echo "Creating virtual environment..."
                bat 'C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe -m venv venv'  // Use double backslashes
                echo "Activating virtual environment..."
                bat 'call venv\\Scripts\\activate.bat'  // This line is fine as is
                echo "Installing dependencies..."
                bat 'C:\\Users\\Lenovo\\AppData\\Local\\Microsoft\\WindowsApps\\pip.exe install -r requirements.txt'  // Use double backslashes
            }
        }
        stage('Run Tests') {
            steps {
                echo "Running tests..."
                // Add your testing commands here, for example:
                // bat 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploying application..."
                // Add your deployment commands here
            }
        }
    }
    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
