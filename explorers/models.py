from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Explorer(models.Model):
    """
    Model that have one-to-one relationship
    to the User model. Extends the information
    we can get about the user
    """
    region_choices = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Antarctica', 'Antarctica'),
        ('Europe', 'Europe'),
        ('Australien', 'Australien')
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=200, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_aezplu'
    )
    region_you_would_like_to_explore = models.CharField(
        max_length=50, choices=region_choices, blank=True
    )
    dream_destination = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Explorer: {self.owner}"

    def create_explorer(sender, instance, created, **kwargs):
        """
        To make sure that an Explorer profile is created
        each time a user is created
        """
        if created:
            Explorer.objects.create(owner=instance)

    post_save.connect(create_explorer, sender=User)


