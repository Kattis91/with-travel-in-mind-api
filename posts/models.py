from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance
    """

    REGION_CHOICES = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Antarctica', 'Antarctica'),
        ('Europe', 'Europe'),
        ('Australien', 'Australien')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default_image_hsxgdj', blank=True
    )
    place = models.CharField(max_length=100, blank=False)
    region = models.CharField(
        max_length=50, choices=REGION_CHOICES, default='', blank=False
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
