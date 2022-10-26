from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient

from gallery.models.image import Image


class ImageDeleteApiTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test user')
        self.token = Token.objects.create(user=self.user)
        self.image1 = Image.objects.create(name='test', slug='test', owner=self.user)

    def test_delete_image_not_owner(self):
        self.assertEqual(1, Image.objects.count())

        user2 = User.objects.create(username='Test user 2')
        token2 = Token.objects.create(user=user2)

        client = APIClient()
        client.force_authenticate(user2, token2)

        url = reverse('image-delete', args=(self.image1.slug, ))

        response = client.delete(url, format='json')

        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(1, Image.objects.count())

    def test_delete_image_not_owner_but_admin(self):
        self.assertEqual(1, Image.objects.count())

        user2 = User.objects.create(username='Test user 2')
        user2.is_staff = True
        user2.save()
        token2 = Token.objects.create(user=user2)

        client = APIClient()
        client.force_authenticate(user2, token2)

        url = reverse('image-delete', args=(self.image1.slug, ))

        response = client.delete(url, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(0, Image.objects.count())

    def test_delete_image_as_owner(self):
        self.assertEqual(1, Image.objects.count())

        client = APIClient()
        client.force_authenticate(self.user, self.token)

        url = reverse('image-delete', args=(self.image1.slug, ))

        response = client.delete(url, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(0, Image.objects.count())
