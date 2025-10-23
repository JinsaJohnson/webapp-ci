# Automated CI Pipeline for a Web Application using Jenkins

## Project Overview
This project demonstrates a fully automated **Continuous Integration (CI) pipeline** using **Jenkins** for a Python Flask web application.  
Whenever new code is pushed to the GitHub repository, Jenkins automatically executes a series of stages including code checkout, dependency installation, testing, build, and artifact packaging.  
The goal is to ensure that the application is always in a ready-to-deploy state, improving automation, reliability, and repeatability following modern DevOps practices.

---

## Tech Stack
- **Language/Framework:** Python Flask  
- **CI Tool:** Jenkins  
- **Version Control:** GitHub  
- **Testing Framework:** Pytest  
- **Package Management:** pip (`requirements.txt`)  

---

## Project Structure
Automated-CI-Pipeline-Jenkins/
├── Jenkinsfile # CI pipeline definition
├── README.md # Project overview and setup guide
├── requirements.txt # Project dependencies
├── setup.py # Python package setup
├── src/ # Application source code
│ └── app.py # Flask main app
├── tests/ # Unit tests
│ └── test_app.py # Pytest test file
├── build/ # Generated build artifacts (by Jenkins)
│ └── artifact.zip
├── artifact.zip # Final build artifact
└── venv/ # Virtual environment (ignored in Git)




---

## Jenkins Pipeline Overview
The pipeline has the following stages:

### 1. **Code Checkout**
- Jenkins automatically pulls the latest code from the GitHub repository.
- Ensures the pipeline always works on the latest code.

### 2. **Install Dependencies**
- Jenkins sets up a Python virtual environment.
- Installs required packages from `requirements.txt` using pip.

### 3. **Run Tests**
- Executes unit tests in `tests/test_app.py` using Pytest.
- Fails the build if any test does not pass.

### 4. **Build**
- Packages the application using `setup.py` into distributable formats (`.tar.gz` and `.whl`).
- Ensures the application is ready for deployment.

### 5. **Package Artifact**
- Zips the project files into `build/artifact.zip` excluding virtual environment, Git metadata, and cache files.

### 6. **Archive**
- Stores the final artifact in Jenkins for download or future deployment.

### 7. **Post Actions**
- Cleans up the workspace.
- Prints success message in the console.

---

## Setup Instructions

### 1. Install Jenkins
- Download Jenkins from [https://www.jenkins.io/download/](https://www.jenkins.io/download/)  
- Follow installation instructions for your OS.  

### 2. Connect Jenkins with GitHub
- Create a new Jenkins pipeline job.
- Add your repository URL: `https://github.com/JinsaJohnson/webapp-ci.git`
- Ensure Jenkins has access to GitHub (public repo works without credentials).

### 3. Create the Pipeline
- Choose **Pipeline** in Jenkins job configuration.
- Set **Pipeline script from SCM** if pulling `Jenkinsfile` from GitHub, or paste your `Jenkinsfile` directly.

### 4. Trigger Builds
- Push changes to the GitHub repository main branch.
- Jenkins automatically triggers the pipeline.
- View the pipeline stages in **Pipeline Stage View**.

---

## Expected Outputs
- **Unit Test Results:** All tests pass (e.g., `test_home`).
- **Build Artifacts:**  
  - `build/artifact.zip`  
  - `dist/webapp_ci-1.0.0-py3-none-any.whl`  
  - `dist/webapp_ci-1.0.0.tar.gz`
- **Console Output:** Shows all pipeline stages executing successfully.

---

## Results / Screenshots
Place screenshots of your Jenkins setup in the `docs/` folder:
- `pipeline_overview.png` – Jenkins pipeline stages view  
- `build_success.png` – Successful build screenshot  
- `test_results.png` – Pytest report screenshot  

---

## Notes
- Ensure Python 3 and pip are installed on the Jenkins server.
- Virtual environment is created and removed during each build for isolation.
- `setup.py` warning is expected due to deprecated `setup.py install`; still works for building artifacts.

---

✅ **Pipeline Status:** Success  
All stages executed successfully, tests passed, and artifact packaged.
