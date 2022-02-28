from django.db.models.signals import post_save
from django.dispatch import receiver

from blog.models import Newsletter


@receiver(post_save, sender=Newsletter)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.display()



