pipeline {
    agent none
    parameters {
        string name: "JOB_NAME",
            description: "The name of the job to create, written in plain english, e.g. \"New Jenkins Job\"",
            defaultValue: ""

        choice name: "AGENT_TYPE",
            choices: ["default", "awscli", "python", "terraform"],
            description: "The scripting language Jenkins will use to run the job"

        choice name: "JOB_MODE",
            choices: ["pipeline", "multibranch"],
            description: "The type of job to create"
    }

    stages {
        stage("Validate Inputs") {
            agent { label "master" }
            steps {
                script {
                    if (params.JOB_NAME == "") {
                        error("Job name must be populated")
                    }

                    def valid_langs = ["default", "awscli", "python", "terraform"]
                    if (! params.AGENT_TYPE in valid_langs) {
                        error("Invalid or unsupported language selected")
                    }

                    def valid_jobtypes = ["pipeline", "multibranch"]
                    if (! params.JOB_MODE in valid_jobtypes) {
                        error("Invalid or unsupported job type selected")
                    }

                    echo "OK"
                }
            }
        }

        stage("Create s3") {
            agent { label "master" }
            environment {
                PYTHONPATH = "${env.WORKSPACE}/lib/jenkinsjob:${env.WORKSPACE}/lib"
            }

            steps {
                 {
                    sh(
                        script: "python3 ${env.WORKSPACE}/bin/s3bucket.py '${params.JOB_NAME}' 2>&1",
                        returnStdout: true
                    )
                }
            }
        }
    }
}
