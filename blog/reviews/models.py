from django.db import models

from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating}/5"
