from rest_framework.serializers import ModelSerializer

from .models import AutoCoverageDetail, AutoPolicyDocument


class AutoDocumentSerializer(ModelSerializer):
    class Meta:
        model = AutoPolicyDocument
        fields = '__all__'
        read_only_fields = (
            'verified',
            'user',
            'rating',
        )

class AutoCoverageSerializers(ModelSerializer):
    class Meta:
        model = AutoCoverageDetail
        fields = '__all__'