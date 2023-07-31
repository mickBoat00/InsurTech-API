from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import AutoCoverageDetail, AutoPolicyDocument
from .serializers import AutoDocumentSerializer


class AutoDocumentView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = AutoPolicyDocument.objects.all()
    serializer_class = AutoDocumentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AutoCoverageView(ListModelMixin, GenericAPIView):
    queryset = AutoCoverageDetail.objects.all()
    serializer_class = AutoDocumentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
