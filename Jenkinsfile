pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git 'https://github.com/priyankasushma13/webhookjenkins.git'
            }
        }
        stage('Build') {
            steps {
                // Build your application (replace this with your build commands)
               steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip3 install flask'
            }
            }
        }
        stage('Deploy') {
            when {
                // Execute this stage only when the branch is 'master'
                branch 'main'
            }
            steps {
                // Deploy your application (replace this with your deployment commands)
                sh 'rsync -avz --delete . /var/www/html'
                sh 'systemctl restart httpd'
            }
        }
    }
    
    post {
        success {
            // Notification for successful build
            slackSend channel: '#builds',
                      color: 'good',
                      message: "Build successful for ${env.BUILD_URL}"
        }
        failure {
            // Notification for failed build
            slackSend channel: '#builds',
                      color: 'danger',
                      message: "Build failed for ${env.BUILD_URL}"
        }
    }
}
