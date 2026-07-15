pipeline {
    agent any
    
    stages {
        stage('Deploy to AWS EC2') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'final-ec2-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                    
                    bat '''
                    icacls "%SSH_KEY%" /remove "BUILTIN\\Users"
                    
                    ssh -o StrictHostKeyChecking=no -i "%SSH_KEY%" %SSH_USER%@ec2-100-59-198-141.compute-1.amazonaws.com "cd YOUR_PROJECT_FOLDER && git pull origin master && docker-compose -f docker-compose-deploy.yml build app && docker-compose -f docker-compose-deploy.yml up --no-deps -d app"
                    '''
                }
            }
        }
    }
}