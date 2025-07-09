from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestPing(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_ping_authenticated(self):
        response = self.client.get(reverse("ping"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('now', response.json())
