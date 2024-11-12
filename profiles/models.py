from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """ 
    Profile model, related to User instance
    """
    crossfit_experience_choices = [
    ('Newbie', 'Newbie'),
    ('1-3 years', '1-3 years'),
    ('3-5 years', '3-5 years'),   
    ('5-8 years', '5-8 years'),  
    ('8-10 years', '8-10 years'),  
    ('OG', 'OG'),  
    ]
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_abuqeh'
    )
    crossfit_experience = models.CharField(
        max_length=30, choices=crossfit_experience_choices, default='Newbie'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)
