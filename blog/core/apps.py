# core/apps.py

from django.apps import AppConfig
import boto3
import os


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Auto-create MinIO bucket on startup
        if os.getenv('DEFAULT_FILE_STORAGE') == 'minio_storage.storage.MinioMediaStorage':
            self.create_minio_bucket()

    def create_minio_bucket(self):
        bucket_name = os.getenv('MINIO_STORAGE_MEDIA_BUCKET_NAME', 'media')
        endpoint = os.getenv('MINIO_STORAGE_ENDPOINT', '127.0.0.1:9000')
        access_key = os.getenv('MINIO_STORAGE_ACCESS_KEY', 'minioadmin')
        secret_key = os.getenv('MINIO_STORAGE_SECRET_KEY', 'minioadmin')
        use_ssl = os.getenv('MINIO_STORAGE_USE_HTTPS', 'False') == 'True'

        s3 = boto3.client(
            's3',
            endpoint_url=f"http{'s' if use_ssl else ''}://{endpoint}",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name='us-east-1',
            verify=use_ssl
        )

        # Create bucket if it doesn't exist
        try:
            existing_buckets = s3.list_buckets()
            if bucket_name not in [b['Name'] for b in existing_buckets['Buckets']]:
                s3.create_bucket(Bucket=bucket_name)
                print(f"✅ Created MinIO bucket: {bucket_name}")
            else:
                print(f"☑️ MinIO bucket already exists: {bucket_name}")
        except Exception as e:
            print(f"❌ Error creating MinIO bucket: {e}")
