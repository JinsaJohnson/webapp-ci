pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                // Pull the latest code from GitHub
                git branch: 'main', url: 'https://github.com/JinsaJohnson/webapp-ci.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Use virtual environment pip to install requirements
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run pytest using virtual environment
                bat 'venv\\Scripts\\pytest --junitxml=test-results.xml'
            }
            post {
                always {
                    // Archive test results
                    junit 'test-results.xml'
                }
            }
        }
        stage('Archive Artifacts') {
            steps {
                // Archive your Flask app files (you can include other files as needed)
                bat 'powershell -Command "Compress-Archive -Path app.py, tests, requirements.txt -DestinationPath artifact.zip"'
                archiveArtifacts artifacts: 'artifact.zip', allowEmptyArchive: false
            }
        }
        stage('Post Actions') {
            steps {
                echo '✅ Build finished!'
            }
        }
    }
}
