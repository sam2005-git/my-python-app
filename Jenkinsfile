pipeline {
   agent any

   environment {
       PYTHON_ENV = 'venv'  // Virtual environment for python
   }

   stages {
       // Stage 1: Clone the repository
       stage('Checkout') {
	    steps {
		    echo 'Cloning repository...'
		    git branch: 'main', url: 'https://github.com/sam2005-git/my-python-app.git'
	    }
	   }

	// Stage 2: Set up the Python environment
	stage('Setup Environment') {
	    steps {
		    echo 'Setting up Python virtual environment...'
		    sh '''
		      python3 -m venv ${PYTHON_ENV}   # Create a virtual environment
		      source ${PYTHON_ENV}/bin/activate   # Activate the virtual environment
		      pip install -r requirements.txt   # Install dependencies
		    '''
	    }
	}
	
	// Stage 3: Run unit tests
	stage('Run Tests') {
	    steps {
		    echo 'Running unit tests...'
		    sh '''
		        source ${PYTHON_ENV}/bin/activate   # Activate the virtual environment
		        pytest tests/   # Run the unit tests using pytest
		    '''
	    }
	}

	// Stage 4: Deploy (this could be to a local HTTP server, for example)
	stage('Deploy') {
	    steps {
		    echo 'Deploying application...'
		    // In this example, we'll simulate deployment by copying the code to a server directory
		    sh '''
		        cp -r * /path/to/local/http/server/root/   # Copy the app to the deployment directory
		    '''
	    }
	}
    }

    post {
       always {
	       echo 'Cleaning up workspace...'
	       cleanWs()   // Clean the workspace after the job finishes
	   }
       success {
	       echo 'Pipeline completed successfully!'
	   }
       failure {
	       echo 'Pipeline failed!'
	   }
     }
}
