import json

from django.test import TestCase
from freezegun import freeze_time
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from .factories import NoteFactory, PatientFactory, UserFactory


class NoteViewsTestCase(TestCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.note_list_url = reverse('core:note-list')

    def test_notes_list(self):
        NoteFactory.create_batch(10)
        NoteFactory.create_batch(3, nutritionist=self.user)
        response = self.client.get(self.note_list_url)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 3)

    @freeze_time('2021-05-04 13:08:03')
    def test_notes_create(self):
        patient = PatientFactory()
        self.user.patients.add(patient)
        response = self.client.post(self.note_list_url,
                                    data={'description': 'This patient is very sick', 'patient': patient.id},
                                    format='json')
        self.user.refresh_from_db()
        note = patient.notes.first()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(self.user.patients.count(), 1)
        self.assertEqual(json.loads(response.content),
                         {'id': note.id,
                          'description': note.description,
                          'patient': patient.id,
                          'nutritionist': self.user.id,
                          'date': '2021-05-04T13:08:03Z'})
