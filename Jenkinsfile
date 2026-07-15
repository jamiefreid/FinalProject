pipeline {
    agent any
    
    stages {
        stage('Deploy to AWS EC2') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'final-ec2-ssh-key', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER')]) {
                    
                    bat '''
                    :: Forcefully break inheritance and remove all inherited permissions
                    icacls "%SSH_KEY%" /inheritance:r
                    
                    :: Grant strict read-only access exclusively to the active Jenkins user
                    icacls "%SSH_KEY%" /grant:r "%USERNAME%:R"
                    
                    :: Execute the SSH deployment using the --build flag to update the entire cluster
                    ssh -o StrictHostKeyChecking=no -i "%SSH_KEY%" %SSH_USER%@ec2-100-59-198-141.compute-1.amazonaws.com "cd FinalProject && git pull origin master && docker-compose -f docker-compose-deploy.yml up -d --build"
                    '''
                }
            }
        }
    }
}