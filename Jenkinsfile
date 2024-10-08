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
                bat 'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv'  // Create virtual environment
                echo "Activating virtual environment..."
                bat 'call venv\\Scripts\\activate.bat'  // Activate the virtual environment
                echo "Installing dependencies..."
                bat 'venv\\Scripts\\pip.exe install -r requirements.txt'  // Install dependencies from requirements.txt
            }
        }
        stage('Run Tests') {
            steps {
                echo "Running tests..."
                // Run your tests here, for example using pytest
                bat 'venv\\Scripts\\pytest'  // Running tests with pytest
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
