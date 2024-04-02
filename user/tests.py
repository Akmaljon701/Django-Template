from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser


class CustomUserAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='admin', password='admin123')
        refresh = RefreshToken.for_user(self.user)
        self.bearer_token = {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_create_user(self):
        data = {
            "first_name": "string",
            "last_name": "string",
            "username": "string",
            "password": "string",
            "role": "string"
        }
        response = self.client.post(reverse('create_user'), data)
        self.assertEquals(response.status_code, 201)

    def test_get_all_users(self):
        response_with_user_id = self.client.get(reverse('get_all_users'), {'user_id': self.user.id})
        response_active_users = self.client.get(reverse('get_all_users'), {'is_active': True})
        response_inactive_users = self.client.get(reverse('get_all_users'), {'is_active': False})
        self.assertEqual(response_with_user_id.status_code, 200)
        self.assertEqual(response_active_users.status_code, 200)
        self.assertEqual(response_inactive_users.status_code, 200)

    def test_get_current_user(self):
        response = self.client.get(reverse('current_user'))
        self.assertEquals(response.status_code, 200)

    def test_update_current_user(self):
        data = {
            "first_name": "string",
            "last_name": "string",
            "username": "string",
            "password": "string",
            "role": "string"
        }
        response = self.client.put(reverse('update_user'), data)
        self.assertEquals(response.status_code, 200)

    def test_delete_current_user(self):
        response = self.client.delete(reverse('delete_user'))
        self.assertEquals(response.status_code, 200)

