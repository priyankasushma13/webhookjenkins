pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git ''
            }
        }
        stage('Build') {
            steps {
                // Build your application (replace this with your build commands)
                sh 'npm install'
                sh 'npm run build'
            }
        }
        stage('Deploy') {
            when {
                // Execute this stage only when the branch is 'master'
                branch 'master'
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
