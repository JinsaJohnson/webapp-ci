pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'       // create virtual environment
                sh './venv/Scripts/pip install -r requirements.txt'  // install packages
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/Scripts/pytest tests/'   // run pytest
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/artifact.zip', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo 'Build Succeeded! ✅'
        }
        failure {
            echo 'Build Failed! ❌'
        }
    }
}
