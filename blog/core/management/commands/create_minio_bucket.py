from django.core.management.base import BaseCommand
from minio import Minio
from django.conf import settings


class Command(BaseCommand):
    help = 'Create MinIO bucket if it doesnt exist'

    def handle(self, *args, **options):
        client = Minio(
            settings.AWS_S3_ENDPOINT_URL.replace('http://', ''),
            access_key=settings.AWS_ACCESS_KEY_ID,
            secret_key=settings.AWS_SECRET_ACCESS_KEY,
            secure=False
        )

        if not client.bucket_exists(settings.AWS_STORAGE_BUCKET_NAME):
            client.make_bucket(settings.AWS_STORAGE_BUCKET_NAME)
            self.stdout.write(f"Created bucket {settings.AWS_STORAGE_BUCKET_NAME}")