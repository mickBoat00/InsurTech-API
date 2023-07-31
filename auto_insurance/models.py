import random

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.
class AutoPolicyDocument(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField(max_length=4)
    vin = models.CharField(max_length=17, unique=True)   
    usage = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auto_documents')
    rating = models.PositiveIntegerField(null=True, blank=True)
    verified = models.BooleanField(default=False)

    def rate_document(self):
        self.rating = random.randrange(0, 110, 10)

    def __str__(self):
        return f"{self.make} {self.model} {self.vin}"
    
@receiver(pre_save, sender=AutoPolicyDocument)
def rating_document(sender, instance, *args, **kwargs):
    if instance.verified:
        instance.rate_document()


@receiver(post_save, sender=AutoPolicyDocument)
def create_coverages(sender, created, instance, *args, **kwargs):
    """ Create coverage for each document verified."""
    if instance.verified:
        if not AutoCoverageDetail.objects.filter(auto_documents=instance).exists():
            AutoCoverageDetail.objects.bulk_create([
                AutoCoverageDetail(auto_documents=instance), 
                AutoCoverageDetail(auto_documents=instance),
                AutoCoverageDetail(auto_documents=instance)
            ])

        
class AutoCoverageDetail(models.Model):
    body_liability_per_person = models.PositiveIntegerField(null=True, blank=True, help_text="Amount paid per person involved")
    total_body_liability = models.PositiveIntegerField(null=True, blank=True, help_text="Total amount for all parties involved")
    property_damage_liability = models.PositiveIntegerField(null=True, blank=True,help_text="Total amount paid for other party propert damage.")
    comprehensive = models.BooleanField(default=False,help_text="Non collision incident ie theft, fire, vandalism")
    collision = models.BooleanField(default=False)
    auto_documents = models.ForeignKey(AutoPolicyDocument, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
