import json

from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from .factories import PatientFactory, UserFactory


class PatientViewsTestCase(TestCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.patient_list_url = reverse('core:patient-list')

    def test_patients_list(self):
        PatientFactory.create_batch(10)
        patients = PatientFactory.create_batch(3)
        self.user.patients.set(patients)
        response = self.client.get(self.patient_list_url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    def test_patients_create(self):
        response = self.client.post(self.patient_list_url,
                                    data={'first_name': 'Jean', 'last_name': 'Bob', 'email': 'jean.bob@bobjean.com'},
                                    format='json')
        self.user.refresh_from_db()
        patient = self.user.patients.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user.patients.count(), 1)
        self.assertEqual(json.loads(response.content),
                         {'id': patient.id,
                          'first_name': patient.first_name,
                          'last_name': patient.last_name,
                          'email': patient.email,
                          'notes': []})
