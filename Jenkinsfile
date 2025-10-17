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
                // create virtual env, upgrade pip, install requirements
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                python -m pip install --upgrade pip setuptools wheel
                if [ -f requirements.txt ]; then
                  pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PYTHONPATH:$PWD
                pytest --maxfail=1 -q
                '''
            }
        }

        stage('Build') {
            steps {
                // Build wheel/sdist if possible. Otherwise create a source snapshot in artifacts/.
                sh '''
                . venv/bin/activate
                mkdir -p artifacts

                if [ -f pyproject.toml ]; then
                  python -m pip install --upgrade build
                  python -m build --no-isolation
                  cp dist/* artifacts/ || true
                elif [ -f setup.py ]; then
                  python setup.py sdist bdist_wheel
                  cp dist/* artifacts/ || true
                else
                  echo "No pyproject.toml or setup.py - creating a source snapshot"
                  # include only the files you need in the package (adjust as necessary)
                  tar -czf artifacts/source.tar.gz --exclude='venv' --exclude='.git' --exclude='__pycache__' .
                fi

                # include requirements.txt (optional)
                if [ -f requirements.txt ]; then
                  cp requirements.txt artifacts/ || true
                fi

                ls -la artifacts
                '''
            }
        }

        stage('Package Artifact') {
            steps {
                sh '''
                # create a clean artifact zip that contains built outputs only
                rm -f artifact.zip
                zip -r artifact.zip artifacts -x "artifacts/venv/*" "artifacts/*.pyc"
                '''
            }
        }

        stage('Archive') {
            steps {
                // Archive both the zip and any files in dist for convenience
                archiveArtifacts artifacts: 'artifact.zip, artifacts/**, dist/**', allowEmptyArchive: false
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Build finished!'
            }
        }
    }

    post {
        always {
            // print workspace and cleanup venv to keep agent tidy
            sh 'echo "Workspace contents:" && ls -la'
            sh 'rm -rf venv || true'
        }
    }
}
