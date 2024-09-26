pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'  // Assign environment variable for virtual environment
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                script {
                    echo "Setting up Python environment: ${PYTHON_ENV}"
                    // Set up the virtual environment
                    sh 'python3 -m venv ${PYTHON_ENV}'
                    // Activate the virtual environment (depending on your shell)
                    sh '. ${PYTHON_ENV}/bin/activate'
                    // Upgrade pip
                    sh 'pip install --upgrade pip'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo 'Installing project dependencies...'
                    // Install dependencies, assuming you have a requirements.txt file
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Linting') {
            steps {
                script {
                    echo 'Running linting...'
                    // Run a linter such as flake8
                    sh 'flake8 .'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    echo 'Running unit tests...'
                    // Run unit tests using a test framework like pytest
                    sh 'pytest'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building the project...'
                    // Add build steps here if applicable (e.g., creating a package or docker image)
                    sh 'python setup.py build'
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    echo 'Packaging the project...'
                    // Package the project, for example, into a wheel or tarball
                    sh 'python setup.py sdist bdist_wheel'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the project...'
                    // Add deployment steps here if applicable
                    // Example: pushing to a production server or a package repository
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Cleaning up...'
                // Deactivate and remove the virtual environment after the pipeline run
                sh 'deactivate || true'  // Ensure deactivate does not fail the build
                sh 'rm -rf ${PYTHON_ENV}'
            }
        }

        success {
            script {
                echo 'Pipeline completed successfully!'
            }
        }

        failure {
            script {
                echo 'Pipeline failed. Check the logs for details.'
            }
        }
    }
}


            
           
