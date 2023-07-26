from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import AutoPolicyDocument
from .serializers import AutoDocumentSerializer


class AutoDocuments(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = AutoPolicyDocument.objects.all()
    serializer_class = AutoDocumentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        print(self.request.auth)
        # print(dir(self.request))
        serializer.save(user=self.request.user)