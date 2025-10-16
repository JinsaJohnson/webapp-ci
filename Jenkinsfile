pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/JinsaJohnson/webapp-ci.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'             // create virtual environment
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && pytest'
            }
        }
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/artifact.zip', allowEmptyArchive: true
            }
        }
        stage('Post Actions') {
            steps {
                echo 'Build finished!'
            }
        }
    }
}
