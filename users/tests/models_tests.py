from io import BytesIO
from PIL import Image
from django.test import TestCase
from django.core.files.base import File
from django.contrib.auth.models import User


from users.models import Profile


def create_test_image(
    name="test.jpg", ext="JPEG", size=(1600, 1500), color=(256, 0, 0)
):
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


class TestProfileModels(TestCase):
    def setUp(self):
        self.user_test = User.objects.create_user(
            username="Test1", password="asdasdasd12312", email="asda@o2.pl"
        )

    def test_profile_creation(self):
        user = User.objects.create(username="taskbuster", password="django-tutorial")

        # Check that a Profile instance has been crated
        self.assertIsInstance(user.profile, Profile)

        # check that it doesn't try to create another profile instace
        user.save()
        self.assertIsInstance(user.profile, Profile)

    def test_profile_username(self):
        self.assertEqual(self.user_test.profile.user.username, "Test1")

    def test_profile_image_default(self):
        self.assertEqual(self.user_test.profile.image, "profile_image/default.jpg")

    def test_profile_image_size(self):
        self.assertLessEqual(self.user_test.profile.image.width, 300)

    def test_profile_image_height_size(self):
        self.assertLessEqual(self.user_test.profile.image.height, 300)
