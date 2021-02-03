import os

import boto3
import pandas as pd


class Repository:

    @staticmethod
    def get_csv_from_s3(bucket_name, object_key):
        client = boto3.client('s3', aws_access_key_id=os.getenv("AWS_ID"),
                              aws_secret_access_key=os.getenv("AWS_SECRET"))

        csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
        return pd.read_csv(csv_obj['Body'])
