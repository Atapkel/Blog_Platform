# Generated by Django 5.2 on 2025-05-01 10:43

import core.media_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_category_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=core.media_storage.MediaStorage(), upload_to='post_images/'),
        ),
    ]
