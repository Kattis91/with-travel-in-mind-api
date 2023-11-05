from django.db import models
from django.contrib.auth.models import User


class Favourite(models.Model):
    """
    Model for favourites (explorers you like extra)
    """
    owner = models.ForeignKey(
        User, related_name='favoriting', on_delete=models.CASCADE)
    favorited = models.ForeignKey(
        User, related_name='favorited', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'favorited']

    def __str__(self):
        return f'{self.owner} {self.favorited}'
