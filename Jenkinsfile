pipeline{
    agent any 

    environment {
        PYTHON_ENV == 'venv'     // Virtual Environment for Python
        
    }
    stages {
        // Stage 1: Clone the repository
        stage('Checkout'){
            steps{
                echo 'Cloneing repository...'
                git branch: 'main', url: 'https://github.com/sam2005-git/my-python-app.git'
            }
        }

        // Stage 2: Set up the Python enviroment

        stage('Setup Environment') {
            steps {
                echo 'Setting up python virtula enviroment...'
                sh '''
                python3 -m venv ${PYTHON_ENV}      # create a virtual environment
                source ${PYTHON_ENV}/bin/activate   # Activate the virtual environment
                pip install -r requirements.txt   # Install dependencies
                '''
            }
        }

        // Stage 3: Run the tests
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh  '''
                source ${PYTHON_ENV}/vin/activate
                pytest tests/
                '''
            }
            
        }

        // Stage 4: Deploy (this could be to a local http server, for example)
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // In this example, we'll simulate deployment by copying the code to a server directory
                sh '''
                cp -r * /path/to/local/http/server/root/  # Copy the app to the deployment directory
                '''
            }
        }


        
    }
}

post {
    always {
        echo 'Cleaning up workspace...'
        cleanWs()     // Clean the workspace after the pipeline execution
    }
    success {
        echo 'Pipeline completed successfully!'
    }
    failure {
        echo 'Pipeline failed!'
    }
}
