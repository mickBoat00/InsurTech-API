from django.urls import path

from .views import AutoCoverageView, AutoDocumentView

urlpatterns = [
    path("documents/", AutoDocumentView.as_view(), name="auto-documents"),
    path("coverages/", AutoCoverageView.as_view(), name="auto-coverage"),
]
