pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/JinsaJohnson/webapp-ci.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.py', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Build succeeded! ✅'
        }
        failure {
            echo 'Build failed! ❌'
        }
    }
}
