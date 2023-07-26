from django.urls import path

from .views import AutoDocuments

urlpatterns = [
    path("documents/", AutoDocuments.as_view(), name="auto-documents")
]
