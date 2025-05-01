from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .media_storage import MediaStorage
from urllib.parse import urlparse


class Post(models.Model):
    class CategoryChoices(models.TextChoices):
        TECH = 'Technology'
        LIFE = 'Lifestyle'
        EDU = 'Education'
        OTHER = 'Other'

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post_images/', storage=MediaStorage(), null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=10,
                                choices=CategoryChoices.choices,
                                default=CategoryChoices.OTHER
                                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # @property
    # def image_path(self):
    #     return urlparse(self.image.url).path

    @property
    def image_path(self):
        if self.image and hasattr(self.image, 'url'):
            return urlparse(self.image.url).path
        return None

    @property
    def author_name(self):
        return self.author.get_full_name() or self.author.username

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
