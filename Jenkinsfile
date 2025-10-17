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
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$(pwd)/src
                pytest --maxfail=1 -q
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                . venv/bin/activate
                mkdir -p build
                if [ -f setup.py ]; then
                    pip install setuptools wheel
                    python setup.py sdist bdist_wheel
                    cp dist/* build/ || true
                else
                    echo "setup.py not found, skipping Python package build"
                fi
                '''
            }
        }

        stage('Package Artifact') {
            steps {
                sh '''
                echo "Zipping project files into build/artifact.zip..."
                zip -r build/artifact.zip . -x "venv/*" "*.git*" "__pycache__/*" "*.pytest_cache/*"
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'build/artifact.zip', allowEmptyArchive: false
            }
        }

        stage('Post Actions') {
            steps {
                echo '✅ Build finished successfully!'
            }
        }
    }

    post {
        always {
            sh '''
            echo "Workspace contents:"
            ls -la
            rm -rf venv
            '''
            cleanWs()
        }
    }
}
