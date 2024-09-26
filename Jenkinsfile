pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning repository...'
                git url: 'https://github.com/sam2005-git/my-python-app.git', branch: 'main'
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up the environment...'
                // Add steps to set up your environment, e.g., install dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Add steps to run your tests
                sh 'python -m unittest discover'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add steps to deploy your application
                sh 'echo "Deploying to production server"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
            cleanWs() // Clean the workspace after failure
        }
    }
}

   
