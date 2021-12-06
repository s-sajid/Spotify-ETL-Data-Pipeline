import os
import boto3

from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

client = boto3.client("s3", 
    aws_access_key_id = os.getenv("AWS_Access_Key"),
    aws_secret_access_key = os.getenv("AWS_Secret_Key"))

date = datetime.now()
filename = f"{date.year}/{date.month}/{date.day}/rapcaviar_albums.csv"

for file in os.listdir():
    if ".csv" in file:
        upload_file_bucket = "s3-uploader-bucket-1"
        upload_file_key = str(filename)
        client.upload_file(file, upload_file_bucket, upload_file_key)



