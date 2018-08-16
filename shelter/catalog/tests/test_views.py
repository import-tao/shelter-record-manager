from django.urls import reverse
from django.test import TestCase
from datetime import datetime
from catalog.models import AnimalInstance, Building, Allergies, Medication
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
        Allergies.objects.create(
            allergy = 'Wheat'
        )
        Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p'
        )


    def test_app_home_view_status_code(self):
        url = reverse('home_page')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_adopted_animals_view_status_code(self):
        url = reverse('adopted_animals')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_create_view_status_code(self):
        url = reverse('animal_create')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_detail_status_code(self):
        url = reverse('animal_detail', kwargs={'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_instance_update_view_status_code(self):
        url = reverse('animal_instance_update', kwargs={'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_instance_delete_view_status_code(self):
        url = reverse('animal_instance_delete',kwargs={'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_adopt_new_view_status_code(self):
        url = reverse('adopt_new',kwargs= {'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_adopt_existing_view_status_code(self):
        url = reverse('adopt_existing',kwargs= {'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_cage_detail_view_status_code(self):
        url = reverse('cage_detail')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_cage_create_view_status_code(self):
        url = reverse('cage_create')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_animal_cage_update_view_status_code(self):
        url = reverse('cage_update',kwargs= {'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)
    
    def test_app_animal_cage_delete_view_status_code(self):
        url = reverse('cage_delete',kwargs= {'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_allergy_list_view_status_code(self):
        url = reverse('allergy_list')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_allergy_create_view_status_code(self):
        url = reverse('allergy_create')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_allergy_delete_view_status_code(self):
        url = reverse('allergy_delete', kwargs={'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_medication_list_view_status_code(self):
        url = reverse('medication_list')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_medication_create_view_status_code(self):
        url = reverse('medication_create')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_app_medication_delete_view_status_code(self):
        url = reverse('medication_delete', kwargs = {'pk':1})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)


