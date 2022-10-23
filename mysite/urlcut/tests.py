from django.test import TestCase
from urlcut.models import Link


class ModelsTestCase(TestCase):

    def test_Package_model(self):
        """Link model work properly"""
        link = Link.objects.create(original_link='https://www.google.pl/',)
        self.assertEqual(link.original_link, 'https://www.google.pl/')

class ViewsTestCase(TestCase):

    def test_Link_model(self):
        """Link model work properly"""
        link = Link.objects.create(original_link='https://www.google.pl/',)
        resp = self.client.get(link.shortened_link)
        self.assertEqual(resp.status_code, 301)

    def test_main_page(self):
        """The main page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'URLCutterREST')

    def test_list_page(self):
        """List page loads properly"""
        response = self.client.get('http://127.0.0.1:8000/list/')
        self.assertEqual(response.status_code, 200)

    def test_admin_link_turned_off(self):
        """The admin should be turned-off"""
        resp = self.client.get('http://127.0.0.1:8000/admin/')
        self.assertNotEqual(resp.status_code, 404)

'''
# my first celery test
class CeleryTasksTestCase(TestCase):
 
    def test_add_task(self):
        from mysite.tasks import sample_task
      
        response = sample_task.apply(args=(4, 4)).get()
        self.assertEqual(response, 8)
'''

'''
# REST tests

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ReadUserTest(APITestCase):
    def setUp(self):
        self.package = Package.objects.create(author='Test author', title="Test title")

    def test_can_read_user_list(self):
        response = self.client.get(reverse('package/'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_user_detail(self):
        response = self.client.get(reverse('package-detail', args=[self.package.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''

'''
Test that should be done:
- searching data with fixtures...
- restAPI - search / APIfactories...
'''