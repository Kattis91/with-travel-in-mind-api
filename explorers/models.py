from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Explorer(models.Model):

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
    region = models.CharField(
        max_length=50, choices=region_choices, blank=True
    )
    dream_destination = models.TextField(max_length=200, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Explorer: {self.owner}"
    
    
    def create_explorer(sender, instance, created, **kwargs):
        """
        To make sure that a Explorer profile is created 
        each time a user is created
        """
        if created:
            Explorer.objects.create(owner=instance)
    
    post_save.connect(create_explorer, sender=User)

