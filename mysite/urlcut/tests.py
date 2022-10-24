from django.test import TestCase
from urlcut.models import Link


class ModelsTestCase(TestCase):

    def test_Link_model(self):
        """Link model work properly"""
        link = Link.objects.create(original_link='https://www.google.pl/',)
        self.assertEqual(link.original_link, 'https://www.google.pl/')

    def test_Link_model_premium(self):
        """Link model work properly for premium-custom link"""
        link = Link.objects.create(original_link='https://www.google.pl/', shortened_link='http://127.0.0.1:8000/abc/')
        self.assertEqual(link.original_link, 'https://www.google.pl/')

class ViewsTestCase(TestCase):

    def test_Link_model(self):
        """Link model work properly"""
        link = Link.objects.create(original_link='https://www.google.pl/',)
        resp = self.client.get(link.shortened_link)
        self.assertEqual(resp.status_code, 301)

    def test_homepage(self):
        """The main page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'URLCutterREST')

    def test_list_page(self):
        """List page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/list/')
        self.assertEqual(response.status_code, 200)

    def remove1_page(self):
        """Remove link page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/remove_unused/zerocount/')
        self.assertEqual(response.status_code, 200)

    def remove2_page(self):
        """Remove link page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/remove_unused/minute/')
        self.assertEqual(response.status_code, 200)

    def remove3_page(self):
        """Remove link page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/remove_used/minute/')
        self.assertEqual(response.status_code, 200)

    def remove4_page(self):
        """Remove link page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/remove_used/day/')
        self.assertEqual(response.status_code, 200)

    def remove5_page(self):
        """Remove link page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/remove_unused/all/')
        self.assertEqual(response.status_code, 200)

    def test_admin_link_turned_off(self):
        """The admin should be turned-off"""
        resp = self.client.get('http://127.0.0.1:8000/admin/')
        self.assertNotEqual(resp.status_code, 404)
