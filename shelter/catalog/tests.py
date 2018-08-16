from django.urls import reverse
from django.test import TestCase
from datetime import datetime
from .models import AnimalInstance, Building
# Create your tests here.

class PageResponse(TestCase):
    def setUP(self):
        build = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        AnimalInstance.objects.create(
            name = 'Dexter',
            status = 'a',
            arrival_date = datetime.now().date(),
            gender = 'm',
            cage = build,

        )

    def test_main_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_main_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_main_contact_view_status_code(self):
        url = reverse('contactus')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_main_contact_view_status_code(self):
        url = reverse('features')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
'''
    def test_app_home_view_status_code(self):
        url = reverse('home_page')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_create_view_status_code(self):
        url = reverse('animal_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_cage_detail_view_status_code(self):
        url = reverse('cage_detail')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_detail_view_status_code(self):
        url = reverse('animal_detail', kwargs= {'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_app_animal_instance_update_view_status_code(self):
        url = reverse('animal_instance_update', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_type_update_view_status_code(self):
        url = reverse('animal_type_update',kwargs= {'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_instance_delete_view_status_code(self):
        url = reverse('animal_instance_delete',kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
'''