from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import AutoCoverageDetail, AutoPolicyDocument


@receiver(pre_save, sender=AutoPolicyDocument)
def rating_document(sender, instance, *args, **kwargs):
    if instance.verified == True:
        instance.rate_document()
        AutoCoverageDetail.objects.create(auto_documents=instance)