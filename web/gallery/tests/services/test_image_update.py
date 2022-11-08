from django.contrib.auth.models import User
from django.test import TestCase

from gallery.models.image import Image
from gallery.services import image_update


class ImageUpdateTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test user')
        self.image1 = Image.objects.create(
            name='test',
            url='https://source.unsplash.com/random/300',
            slug='test',
            owner=self.user,
        )

    def test_updating_image_without_tags(self):
        self.assertEqual(1, Image.objects.count())

        data = {
            "name": "new_name",
            "slug": "new_slug",
            "url": "https://source.unsplash.com/random/500",
        }

        updated_image = image_update(
            image=self.image1,
            data=data,
        )

        self.assertEqual(1, Image.objects.count())
        self.assertEqual(updated_image, Image.objects.first())
        self.assertEqual("new_slug", self.image1.slug)
        self.assertEqual("new_name", self.image1.name)
        self.assertEqual("https://source.unsplash.com/random/500", self.image1.url)

    def test_updating_image_with_tags(self):
        self.assertEqual(1, Image.objects.count())

        data = {
            "name": self.image1.name,
            "tags": "tag1",
        }

        updated_image = image_update(
            image=self.image1,
            data=data,
        )
        self.assertEqual(1, Image.objects.count())
        self.assertEqual(updated_image, Image.objects.first())
        self.assertEqual(1, Image.objects.first().tags.count())
