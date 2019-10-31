from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class test_views(TestCase):

    def test_home_url_accessible_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_url_accessible_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_3w_url_accessible_by_name(self):
        response = self.client.get(reverse('three_w'))
        self.assertEqual(response.status_code, 200)

    def test_rules_url_accessible_by_name(self):
        response = self.client.get(reverse('rules'))
        self.assertEqual(response.status_code, 200)

    def test_resources_url_accessible_by_name(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, 200)