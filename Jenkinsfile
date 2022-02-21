pipeline {
    agent any
  
    parameters {
        string(name: 'rolename', defaultValue: 'jenkins_role', description: 'Workspace/environment file to use for deployment')
        string(name: 'accountid', defaultValue: '941039889978', description: 'accountid variable to pass to Terraform')
        string(name: 'region', defaultValue: 'us-east-1', description: 'region variable to pass to Terraform')
        string(name: 'SERVICE_CODE', defaultValue: 'ec2', description: 'service code for eip limit increase')
        string(name: 'QUOTAS_CODE', defaultValue: 'L-0263D0A3', description: 'quota code for eip limit increase')
        string(name: 'DESIRED_LIMIT', defaultValue: '25', description: 'desired number for eip limit increase')
    }
    stages {
        stage('Cloning Git') {
         steps {
             git branch: 'main', url: 'https://github.com/krishna8393/pythonprojects.git'
         }
       }
        stage('Connecting To Aws') {
            steps {
                //sh(
                  //  script: "python3 ${env.WORKSPACE}/bin/s3bucket.py '${params.JOB_NAME}' 2>&1",
                    //returnStdout: true
                //)
                sh "chmod +x ${env.WORKSPACE}/shell/config.sh"
                sh "${env.WORKSPACE}/shell/config.sh '${params.accountid}' '${params.rolename}' '${params.region}' '${params.SERVICE_CODE}' '${params.QUOTAS_CODE}' '${params.DESIRED_LIMIT}'"
                // sh "aws sts get-caller-identity"
            }
        }
    }
}
