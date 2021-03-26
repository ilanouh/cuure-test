from django.core.management.base import BaseCommand
from core.tests.factories import NoteFactory, PatientFactory, UserFactory


class Command(BaseCommand):
    help = 'Populate DB'

    def handle(self, *args, **options):
        user = UserFactory(username="admin")
        patients = PatientFactory.create_batch(20)
        user.patients.set(patients)
        for patient in patients:
            NoteFactory.create_batch(5, nutritionist=user, patient=patient)
        NoteFactory.create_batch(50)
