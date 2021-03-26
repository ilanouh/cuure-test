from rest_framework import viewsets

from core.models import Note, Patient
from core.serializers import NoteSerializer, PatientSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(nutritionist=self.request.user)
        return queryset.select_related('patient', 'nutritionist')


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(nutritionists=self.request.user)
        return queryset.prefetch_related('nutritionists', 'notes')
