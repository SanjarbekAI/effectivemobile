from django.contrib.auth import get_user_model
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


@override_settings(CSRF_COOKIE_HTTPONLY=False, CSRF_COOKIE_SECURE=False)
class LoginAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword", role="ORDINARY")
        self.login_url = "/api/v1/users/login/"

    def test_valid_login(self):
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpassword"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access_token", response.data)
        self.assertIn("refresh_token", response.data)
        self.assertEqual(response.data["user"]["role"], "admin")

    def test_invalid_login(self):
        response = self.client.post(self.login_url, {"username": "wronguser", "password": "wrongpassword"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
