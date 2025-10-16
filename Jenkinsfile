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
        sh '''
        . venv/bin/activate
        export PYTHONPATH=$PYTHONPATH:$PWD
        pytest
        '''
    }
}

stage('Build Artifact') {
            steps {
                sh '''
                echo "Zipping project files into artifact.zip..."
                zip -r artifact.zip . -x "venv/*" "*.git*" "__pycache__/*"
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'artifact.zip', allowEmptyArchive: false
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Build finished!'
            }
        }
    }
}
