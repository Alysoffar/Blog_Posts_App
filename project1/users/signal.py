from django.db.models.signals import post_save # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.dispatch import receiver # type: ignore
from .models import Profile

@receiver(post_save, sender=User)
def creat_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def creat_profile(sender, instance, created, **kwargs):
    instance.profile.save()