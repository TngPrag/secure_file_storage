from fs.storage import store_file_in_filesystem, store_file_in_s3

def create_encrypted_file_local(file_name, data):
    """Store an encrypted file in the local filesystem."""
    store_file_in_filesystem(file_name, data)

def create_encrypted_file_aws_s3(file_name, data):
    """Store an encrypted file in AWS S3."""
    store_file_in_s3(file_name, data)
