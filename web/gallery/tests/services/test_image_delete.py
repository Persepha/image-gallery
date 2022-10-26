from django.contrib.auth.models import User
from django.test import TestCase

from gallery.models.image import Image
from gallery.services import image_delete


class ImageDeleteTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test user')
        Image.objects.create(
            name='test',
            slug='test',
            owner=self.user,
        )

    def test_deleting_image(self):
        self.assertEqual(1, Image.objects.count())
        image_delete(image=Image.objects.first())
        self.assertEqual(0, Image.objects.count())
