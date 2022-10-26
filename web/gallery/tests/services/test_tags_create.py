from django.test import TestCase

from gallery.models.tag import Tag
from gallery.services import tags_create


class TagsCreateTests(TestCase):
    def setUp(self) -> None:
        self.tag1 = Tag.objects.create(title='test')

    def test_create_tags_with_existing_tags(self):
        self.assertEqual(1, Tag.objects.count())
        tags = 'test'

        tag_list = tags_create(tags=tags)

        self.assertEqual(1, Tag.objects.count())
        self.assertQuerysetEqual(
            Tag.objects.all(),
            tag_list,
            ordered=False,
        )

    def test_create_tags_with_new_tags(self):
        self.assertEqual(1, Tag.objects.count())
        tags = 'bla, test'

        tag_list = tags_create(tags=tags)

        self.assertEqual(2, Tag.objects.count())
        self.assertQuerysetEqual(
            Tag.objects.all(),
            tag_list,
            ordered=False,
        )
