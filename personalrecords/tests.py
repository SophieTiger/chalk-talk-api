from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import PersonalRecord
from datetime import date


class PersonalRecordTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='testuser1', password='testpass123')
        self.user2 = User.objects.create_user(username='testuser2', password='testpass123')
        self.client.force_authenticate(user=self.user1)

    def test_create_personal_record(self):
        data = {
            'exercise': 'Bench Press',
            'weight': 100.5,
            'reps': 5,
            'date_achieved': '2024-12-16',
            'notes': 'New personal best!'
        }
        response = self.client.post('/personalrecords/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PersonalRecord.objects.count(), 1)
        self.assertEqual(PersonalRecord.objects.get().owner, self.user1)

    def test_update_personal_record(self):
        pr = PersonalRecord.objects.create(
            owner=self.user1,
            exercise='Squat',
            weight=150.0,
            reps=3,
            date_achieved=date(2024, 12, 1)
        )
        data = {'weight': 160.0, 'reps': 4}
        response = self.client.patch(f'/personalrecords/{pr.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pr.refresh_from_db()
        self.assertEqual(pr.weight, 160.0)
        self.assertEqual(pr.reps, 4)

    def test_delete_personal_record(self):
        pr = PersonalRecord.objects.create(
            owner=self.user1,
            exercise='Deadlift',
            weight=200.0,
            reps=1,
            date_achieved=date(2024, 12, 15)
        )
        response = self.client.delete(f'/personalrecords/{pr.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(PersonalRecord.objects.count(), 0)

    def test_list_personal_records(self):
        PersonalRecord.objects.create(
            owner=self.user1,
            exercise='Bench Press',
            weight=100.0,
            reps=5,
            date_achieved=date(2024, 12, 16)
        )
        PersonalRecord.objects.create(
            owner=self.user2,
            exercise='Squat',
            weight=150.0,
            reps=3,
            date_achieved=date(2024, 12, 15)
        )
        response = self.client.get('/personalrecords/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
