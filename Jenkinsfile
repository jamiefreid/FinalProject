pipeline {
    agent any
    
    stages {
        stage('Deploy to AWS EC2') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                    
                    bat '''
                    ssh -o StrictHostKeyChecking=no -i %SSH_KEY% %SSH_USER%@ec2-100-59-198-141.compute-1.amazonaws.com "cd FinalProject && git pull origin master && docker-compose -f docker-compose-deploy.yml build app && docker-compose -f docker-compose-deploy.yml up --no-deps -d app"
                    '''
                }
            }
        }
    }
}