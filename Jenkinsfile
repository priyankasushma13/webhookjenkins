pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                git 'https://github.com/priyankasushma13/webhookjenkins.git'
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install flask'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'ngrok http 5000'
                sh 'python3 app.py &'
            }
        }
    }
  post {
        success {
            echo 'Deployment successful'
        }
        failure {
            echo 'Deployment failed'
        }
    }
}
