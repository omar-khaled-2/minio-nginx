import os
from utils.secret import secret
from boto3 import client

from botocore.config import Config
from minio import Minio




print(os.getenv("MINIO_ENDPOINT"))
def main():
    s3_client = client(
        's3',
        endpoint_url=os.getenv("MINIO_ENDPOINT"),
        aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
        aws_secret_access_key=secret.get("MINIO_PASSWORD"),
        region_name='us-east-1',
        config=Config(signature_version='s3v4')
    )
    print(os.getenv("MINIO_ROOT_USER"), secret.get("MINIO_PASSWORD"))

    print("Creating bucketss")
    s3_client.create_bucket(Bucket='tests')

    # while True:
    #     print("")
    #     try:
    #     except Exception as e:
    #         print(e)
    # pass
    # s3_client.create_bucket(Bucket='test')
    
try:
    main()
except Exception as e:
    print(e)