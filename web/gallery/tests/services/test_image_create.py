from django.contrib.auth.models import User
from django.test import TestCase

from gallery.models.image import Image
from gallery.services import image_create


class ImageCreateTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test user')

    def test_creating_image_without_tags(self):
        self.assertEqual(0, Image.objects.count())
        created_image = image_create(
            name='test',
            slug='test',
            owner=self.user,
        )
        self.assertEqual(1, Image.objects.count())
        self.assertEqual(created_image, Image.objects.first())

    def test_creating_image_with_tags(self):
        self.assertEqual(0, Image.objects.count())
        created_image = image_create(
            name='test',
            slug='test',
            owner=self.user,
            tags='testtag1, testtag2,',
        )
        self.assertEqual(1, Image.objects.count())
        self.assertEqual(created_image, Image.objects.first())
        self.assertEqual(2, Image.objects.first().tags.count())
