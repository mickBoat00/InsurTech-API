from rest_framework.serializers import ModelSerializer

from .models import AutoPolicyDocument


class AutoDocumentSerializer(ModelSerializer):
    class Meta:
        model = AutoPolicyDocument
        fields = '__all__'
        read_only_fields = (
            'verified',
            'user',
            'rating',
        )