import boto3
import json
import time
import sys
import os

accountid = os.getenv("accountid")
region = os.getenv("region")
trg_accountid = os.getenv("trg_accountid")
ec2_client = boto3.client('ec2')

def list_all_buckets():
    # Retrieve the list of existing buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

def amisharing():
    response = ec2_client.describe_images(Owners=['self'])
    print(response)
#     try:
#         for ami in response['Images']:
#             for imageName in ami_list:
#                 if(imageName == ami['Name']):
#                     response2 = ec2_client.modify_image_attribute(
#                         Attribute='launchPermission',
#                         ImageId=ami['ImageId'],
#                         OperationType='add',
#                         UserIds=consumer_account_id
#                     )
#                     print(response2)
#     except Exception as e:
#         print(e)

if __name__ == "__main__":
#     list_all_buckets()
    print('accountid:', accountid)
    print('region:', region)
    print('target account id:', trg_accountid)
    amisharing()
