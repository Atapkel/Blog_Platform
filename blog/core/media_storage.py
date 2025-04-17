from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    bucket_name = 'media'  # This must match your bucket name in MinIO
    custom_domain = False  # So MEDIA_URL is respected
