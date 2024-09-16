# fs/storage.py
import boto3
from configs.config import get_config

import os

def store_file_in_filesystem(file_name, data):
    """Store the encrypted file in the local file system."""
    # Ensure the file_system directory exists
    if not os.path.exists('file_system'):
        os.makedirs('file_system')
    
    file_path = os.path.join('file_system', f'encrypted_{file_name}')
    with open(file_path, 'wb') as f:
        f.write(data)


def store_file_in_s3(file_name, data):
    """Store the encrypted file in AWS S3."""
    s3 = boto3.client(
        's3',
        aws_access_key_id=get_config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=get_config('AWS_SECRET_ACCESS_KEY'),
        region_name=get_config('AWS_REGION')
    )
    s3.put_object(
        Bucket=get_config('AWS_S3_BUCKET'),
        Key=f'encrypted_{file_name}',
        Body=data
    )

def save_to_storage(file_data, file_name, storage_type='local'):
    """Save the file data to the specified storage type (local or S3)."""
    if storage_type == 's3':
        store_file_in_s3(file_name, file_data)
    else:
        store_file_in_filesystem(file_name, file_data)
