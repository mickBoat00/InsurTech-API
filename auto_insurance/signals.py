from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import AutoPolicyDocument


@receiver(pre_save, sender=AutoPolicyDocument)
def rating_document(sender, instance, *args, **kwargs):
    instance.rate_document()