from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.models import User, Freelancer, BusinessOwner


@receiver(post_save, sender=User)
def create_related_model(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Type.FREELANCER:
            Freelancer.objects.create(user=instance)
        elif instance.role == User.Type.BUSINESS_OWNER:
            BusinessOwner.objects.create(user=instance)
