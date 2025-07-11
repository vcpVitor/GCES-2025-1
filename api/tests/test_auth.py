from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse


class TestToken(TestCase):
    fixtures = ["users"]

    def setUp(self):
        self.client = APIClient()

    def test_token_success(self):
        url = reverse("token")
        resp = self.client.post(
            url,
            {"username": "jeff", "password": "sifjo123909201jdasd"}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn("access", resp.data)
        self.assertIn("refresh", resp.data)

    def test_token_error(self):
        url = reverse("token")
        resp = self.client.post(
            url,
            {"username": "jeff", "password": "foo"}
        )
        self.assertEqual(resp.status_code, 401)
