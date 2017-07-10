from boto.s3.connection import S3Connection
from boto.s3.key import Key
from settings import aws_access_key, aws_secret_key, bucket_name


def upload_file_to_s3(filename, key):
    conn = S3Connection(aws_access_key, aws_secret_key)
    bucket = conn.get_bucket(bucket_name)
    k = Key(bucket)
    k.key = key
    k.set_contents_from_filename(filename)
    k.make_public()
    return 'https://{bucket}.s3.amazonaws.com{key}'.format(
        bucket=bucket.name,
        key=key
    )
