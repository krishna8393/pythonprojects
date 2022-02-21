# aws sts assume-role --role-arn arn:aws:iam::$accountid:role/$rolename --role-session-name jenkins-agent --duration-seconds 3600 --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text
# aws sts get-caller-identity

export $(
printf "AWS_ACCESS_KEY_ID=%s AWS_SECRET_ACCESS_KEY=%s AWS_SESSION_TOKEN=%s" $(
aws sts assume-role --role-arn arn:aws:iam::$accountid:role/$rolename --role-session-name jenkins-agent --duration-seconds 3600 --query "Credentials.[AccessKeyId,SecretAccessKey,SessionToken]" --output text
)
)

python3 /var/lib/jenkins/workspace/s3-python/bin/s3bucket.py '${params.accountid}' '${params.region}' '${params.SERVICE_CODE}' '${params.QUOTAS_CODE}' '${params.DESIRED_LIMIT}'

# terraform init
# terraform plan
# terraform apply --auto-approve
