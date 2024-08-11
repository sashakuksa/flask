pipeline {
agent any
environment {
PYTHON_ENV = 'development'
}
stages {
stage('Checkout') {
steps {
git branch: "${env.BRANCH_NAME}", url: 'https://github.com/sashakuksa/flask'
}
}
stage('Setup Python') {
steps {
sh 'python3 -m venv venv'
sh '. venv/bin/activate'
}
}
stage('Install Dependencies') {
steps {
sh '. venv/bin/activate && pip install -r requirements/dev.txt'
}
}
stage('Build') {
steps {
sh '. venv/bin/activate && python setup.py install'
}
}
stage('Test') {
steps {
sh '. venv/bin/activate && pytest --junitxml=reports/test-results.xml'
}
post {
always {
junit 'reports/test-results.xml'
archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
}
}
}
stage('Deploy') {
when {
branch 'master'
}
environment {
PYTHON_ENV = 'production'
}
steps {
sh './deploy-prod.sh'
}
}
stage('Deploy') {
when {
branch 'dev'
}
steps {
sh './deploy-dev.sh'
}
}
}
post {
always {
echo 'Pipeline finished.'
}
success {
mail to: 'team@example.com',
subject: "SUCCESS: ${currentBuild.fullDisplayName}",
body: "Good news! The build ${currentBuild.fullDisplayName} completed successfully."
}
failure {
mail to: 'team@example.com',
subject: "FAILURE: ${currentBuild.fullDisplayName}",
body: "Bad news! The build ${currentBuild.fullDisplayName} failed. Please check the Jenkins logs for more details."
}
}
}
