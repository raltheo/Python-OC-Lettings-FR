from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import Profile
from .views import profiles_index, profile


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test_user")
        self.profile = Profile.objects.create(user=self.user, favorite_city="New York")

    def tearDown(self):
        self.profile.delete()
        self.user.delete()

    def test_profiles_index_view(self):
        request = RequestFactory().get("/")
        response = profiles_index(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        request = RequestFactory().get("/")
        response = profile(request, username="test_user")
        self.assertEqual(response.status_code, 200)
