from django.contrib import admin

# Register your models here.
from .models import AutoCoverageDetail, AutoPolicyDocument

admin.site.register(AutoCoverageDetail)
admin.site.register(AutoPolicyDocument)