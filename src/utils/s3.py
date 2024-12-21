import boto3
from botocore.exceptions import ClientError


def create_s3_client(endpoint_url, access_key, secret_key):
    """
    Creates and returns an S3 client.
    """
    return boto3.client(
        service_name='s3',
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )


def create_bucket(s3_client, bucket_name):
    """
    Creates a bucket if it does not already exist.
    """
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        raise Exception(f"Failed bucket creation: {e}")


def bucket_exists(s3_client, bucket_name):
    """
    Checks if a bucket exists.
    """
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def upload_object(s3_client, bucket_name, object_key, object_data):
    """
    Uploads an object to the specified bucket.
    """
    try:
        s3_client.put_object(Bucket=bucket_name, Key=object_key, Body=object_data)
    except Exception as e:
        raise e
