import boto3
import json
import time
import sys
import os

accountid = os.getenv("accountid")
region = os.getenv("region")
trg_accountid = os.getenv("trg_accountid")

def list_all_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')



if __name__ == "__main__":
#     list_all_buckets()
    print('accountid:', accountid)
    print('region:', region)
    print('target account id:', trg_accountid)
