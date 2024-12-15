from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """Home Page Tests"""

    def test_url_exists_at_correct_location_homepageview(self):
        """Test URL exists at correct location homepageview"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_views(self):
        """Test homepage views"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
