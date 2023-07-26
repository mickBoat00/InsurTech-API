import random

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.
class AutoPolicyDocument(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    vin = models.CharField(max_length=17)   
    usage = models.CharField(max_length=50)
    mileage = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    rating = models.IntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)

    def rate_document(self):
        self.rating = random.randrange(0, 110, 10)

    def __str__(self):
        return f"{self.make} {self.model} {self.vin}"

@receiver(pre_save, sender=AutoPolicyDocument)
def rating_document(sender, instance, *args, **kwargs):
    instance.rate_document()