pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'        // Virtual environment for python
    }

    stages {
        // Stage 1 : Clone the repository
        stage('checkout') {
            steps {
                echo 'Cloning repository...'
                git branch: 'main' , url: 'https://github.com/sam2005-git/my-python-app.git'
            }
        }

        // stages 2 : Set up the python environment
        stage('setup Environment'){
            steps{
                echo 'Setting up python virtual environment...'
                sh'''
                   python3 -m venv ${PYTHON_ENV}
                   source ${PYTHON_ENV}/bin/activate
                   pip install -r requirments.txt
                '''  
            }
        }

        // Stage 3 : Run unit tests
        stage('Run Tests') {
            steps{
                echo 'Running unit tests...'
                sh'''
                   source ${PYTHON_ENV}/bin/activate
                   pytest tests/
                '''   
            }
        }

        //Stage 4 : Deploy (this could be to a local HTTP server,for example)
        stage('Deploy'){
            steps{
                echo 'Deploying application...'
                // In this example, we will stimute deployment by copying the code to a server directory
                sh'''
                   cp -r * /path/to/local/http/server/root/ # copy the app to the deployment directory
                '''
            }
        }
    }

    post{
        always {
            echo 'Cleaning up workspace...'   
            cleanWs()                                                         // clean the workspace after the pipeline finish
        }
        success{
            echo 'Pipeline completed succesfully!'
        }
        failure{
            echo 'Pipeline failed!'
        }
    }



}

   
