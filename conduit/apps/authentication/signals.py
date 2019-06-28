# This file will not automatically. Therefore we need to create AppConfig
# class for the authentication app and register it with django.
# Therefore we make a class in __init__.py file in authentication app.

# We are making this file because we want to tell django that
# whenever a new `User` is created we need to generate a new
# profile for the user.

from django.db.models.signals import post_save
from django.dispatch import receiver
from conduit.apps.profiles.models import Profile 
from .models import User

@receiver(post_save, sender=User)
def create_related_profiles(sender, instance, created, *args, **kwargs):
    # Notice that we're checking for `created` here. We only want to do this
    # the first time the `User` instance is created. If the save that caused
    # this signal to be run was an update action, we know the user already
    # has a profile.
    if instance and created:
        instance.profile = Profile.objects.create(user=instance)
