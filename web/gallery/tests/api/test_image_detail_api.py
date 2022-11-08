from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from gallery.models.image import Image


class ImageDetailApiTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test user')
        self.image1 = Image.objects.create(
            name='test',
            url='https://source.unsplash.com/random/300',
            slug='test',
            owner=self.user
        )

    def test_get_image_detail(self):
        url = reverse('image-detail', args=(self.image1.slug, ))
        response = self.client.get(url, format='json')

        expected_data = {
            'id': self.image1.id,
            'name': self.image1.name,
            'url': self.image1.url,
            'slug': self.image1.slug,
            'owner_username': self.image1.owner.username,
            'tags': [],
        }

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)
