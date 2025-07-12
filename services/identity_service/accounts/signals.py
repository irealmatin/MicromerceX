from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    automaticly create a profile user when new user register .
    """
    if created:
        UserProfile.objects.create(user=instance)
        print(f"Profile created for user {instance.username}")