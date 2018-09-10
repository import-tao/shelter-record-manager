from django.urls import reverse
from django.test import TestCase


class PageResponse(TestCase):

# These are tests for the main app - Test response is valid 200
    def test_main_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/index.html')


    def test_main_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/about.html')

    def test_main_contact_view_status_code(self):
        url = reverse('contactus')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/contactus.html')
        
    def test_main_features_view_status_code(self):
        url = reverse('features')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/features.html')