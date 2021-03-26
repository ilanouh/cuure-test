from django.urls import path, include
from rest_framework import routers

from core import viewsets

router = routers.DefaultRouter()
router.register(r'notes', viewsets.NoteViewSet)
router.register(r'patients', viewsets.PatientViewSet)


urlpatterns = [
    path('api/', include(router.urls))
]
