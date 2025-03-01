from django.utils import timezone
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from datetime import timedelta

from ..models import AnimalInstance, Building, Allergies, Medication
from ..views import homepage_view
# Create your tests here.

class PageRedirectstoLogin(TestCase):
    ''' Check the url redirects to login page when not logged in,
    and the correct next page.
    '''
    def setUp(self):
        self.building = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        self.animal = AnimalInstance.objects.create(
            name = 'Dexter',
            status = 'a',
            arrival_date = timezone.now(),
            gender = 'm',
            cage = self.building,
        )
        self.allergy = Allergies.objects.create(
            allergy = 'Wheat'
        )
        self.medication = Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p'
        )

    def url_redirect_tests(self, url, template_name='registration/login.html', redirect='/accounts/login/?next=/app/'):
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, redirect)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)
        return response

    def test_app_home_view_status_code(self):
        url = reverse('home_page')
        self.url_redirect_tests(url)
                   
    def test_app_animal_adopted_animals_view_status_code(self):
        url = reverse('adopted_animals')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/adopted/')

    def test_app_animal_create_view_status_code(self):
        url = reverse('animal_create')
        self.url_redirect_tests(url,redirect='/accounts/login/?next=/app/create/')

    def test_app_animal_detail_status_code(self):
        url = reverse('animal_detail', kwargs={'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/1/')

    def test_app_animal_instance_update_view_status_code(self):
        url = reverse('animal_instance_update', kwargs={'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/1/update/')

    def test_app_animal_instance_delete_view_status_code(self):
        url = reverse('animal_instance_delete',kwargs={'pk':1})
        self.url_redirect_tests(url,redirect='/accounts/login/?next=/app/1/delete/')

    def test_app_animal_adopt_new_view_status_code(self):
        url = reverse('adopt_new',kwargs= {'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/adopt/1/')

    def test_app_animal_adopt_existing_view_status_code(self):
        url = reverse('adopt_existing',kwargs= {'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/adopted/1/')

    def test_app_animal_cage_detail_view_status_code(self):
        url = reverse('cage_detail')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/cage/')

    def test_app_animal_cage_create_view_status_code(self):
        url = reverse('cage_create')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/cage/create/')

    def test_app_animal_cage_update_view_status_code(self):
        url = reverse('cage_update',kwargs= {'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/cage/1/')
    
    def test_app_animal_cage_delete_view_status_code(self):
        url = reverse('cage_delete',kwargs= {'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/cage/1/delete/')

    def test_app_allergy_list_view_status_code(self):
        url = reverse('allergy_list')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/allergy/')

    def test_app_allergy_create_view_status_code(self):
        url = reverse('allergy_create')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/allergy/create/')

    def test_app_allergy_delete_view_status_code(self):
        url = reverse('allergy_delete', kwargs={'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/allergy/1/delete/')

    def test_app_medication_list_view_status_code(self):
        url = reverse('medication_list')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/medication/')

    def test_app_medication_create_view_status_code(self):
        url = reverse('medication_create')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/medication/create/')

    def test_app_medication_delete_view_status_code(self):
        url = reverse('medication_delete', kwargs = {'pk':1})
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/app/medication/1/delete/')


class LoggedinResponse(TestCase):
    ''' Check a logged in user gets to the correct page and can perform actions
    '''
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.building = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        current_date = timezone.now()
        self.animal = AnimalInstance.objects.create(
            name = 'Dexter',
            status = 'a',
            arrival_date = current_date,
            gender = 'm',
            cage = self.building,
        )
        self.allergy = Allergies.objects.create(
            allergy = 'Wheat'
        )
        self.medication = Medication.objects.create(
            name = 'Paracetamol',
            type1 = 'p'
        )

    def login_testing(self, url, template, content=""):
        ''' Check logged in user accesses correct template and checks content.
        '''
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(url)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template)
        self.assertContains(response, content)
        return response

    def test_homeview_logged_in_user(self):
        url = reverse('home_page')
        template = 'catalog/homepage.html'
        self.login_testing(url, template)

    def test_app_animal_adopted_animals(self):
        url = reverse('adopted_animals')
        template = 'catalog/adopted_animals.html'
        self.login_testing(url, template)

    def test_app_animal_create_view(self):
        url = reverse('animal_create')
        template = 'catalog/animalcreate.html'
        self.login_testing(url, template)

    def test_app_animal_detail(self):
        url = reverse('animal_detail',kwargs= {'pk':1})
        template = 'catalog/animaldetail.html'
        self.login_testing(url, template)

    def test_app_animal_instance_update(self):
        url = reverse('animal_instance_update',kwargs= {'pk':1})
        template = 'catalog/animal_instance_update.html'
        self.login_testing(url, template)

    def test_app_animal_instance_delete(self):
        url = reverse('animal_instance_delete',kwargs= {'pk':1})
        template = 'catalog/animal_instance_delete.html'
        self.login_testing(url, template)

    def test_app_animal_adopt_new(self):
        url = reverse('adopt_new',kwargs= {'pk':1})
        template = 'catalog/adopt_animal.html'
        self.login_testing(url, template)

    def test_app_animal_adopt_existing(self):
        url = reverse('adopt_existing',kwargs= {'pk':1})
        template = 'catalog/adopted_animal_update.html'
        self.login_testing(url, template)


    def test_app_cage_detail(self):
        url = reverse('cage_detail')
        template =  'catalog/cage_detail.html'
        self.login_testing(url, template)


    def test_app_cage_create(self):
        url = reverse('cage_create')
        template =  'catalog/cage_create.html'
        self.login_testing(url, template)
    
    def test_app_cage_update(self):
        url = reverse('cage_update', kwargs={'pk':1})
        template =  'catalog/cage_update.html'
        self.login_testing(url, template)


    def test_app_cage_delete(self):
        url = reverse('cage_delete', kwargs={'pk':1})
        template =  'catalog/cage_delete.html'
        self.login_testing(url, template)


    def test_app_allergy_list(self):
        url = reverse('allergy_list')
        template =  'catalog/allergies_list.html'
        self.login_testing(url, template)


    def test_app_allergy_create(self):
        url = reverse('allergy_create')
        template =  'catalog/allergy_create.html'
        self.login_testing(url, template)


    def test_app_allergy_delete(self):
        url = reverse('allergy_delete', kwargs={'pk':1})
        template =  'catalog/allergy_delete.html'
        self.login_testing(url, template)

    def test_app_medication_list(self):
        url = reverse('medication_list')
        template =  'catalog/medication_list.html'
        self.login_testing(url, template)

    def test_app_medication_create(self):
        url = reverse('medication_create')
        template =  'catalog/medication_create.html'
        self.login_testing(url, template)

    def test_app_medication_delete(self):
        url = reverse('medication_delete', kwargs={'pk':1})
        template =  'catalog/medication_delete.html'
        self.login_testing(url, template)

    def test_create_animal_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('animal_create')
        current_date = timezone.now()
        data = {
            'name': 'Max',
            'animal_species': 'Dog',
            'breed': 'German Shepherd',
            'status': 'a',
            'arrival_date': current_date,
            'gender': 'm',
            'hair_type': 'f',
            'hair_length': 's',
            'bio': 'A friendly German Shepherd',
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home_page'))
        self.assertTrue(AnimalInstance.objects.filter(name='Max').exists())

    def test_create_animal_post_invalid(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('animal_create')
        data = {
            'name': 'Max',  # Missing required fields
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/animalcreate.html')
        self.assertFalse(AnimalInstance.objects.filter(name='Max').exists())

    def test_adopt_animal_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('adopt_new', kwargs={'pk': self.animal.pk})
        current_date = timezone.now()
        data = {
            'status': 'd',
            'leaving_date': current_date,
            'adopter_first_name': 'John',
            'adopter_last_name': 'Doe',
            'adopter_email': 'john@example.com',
            'adopter_contactnumber1': '1234567890',
        }
        response = self.client.post(url, data)
        if response.status_code != 302:
            print(response.context['form'].errors if 'form' in response.context else "No form in context")
        self.assertRedirects(response, reverse('home_page'))
        self.animal.refresh_from_db()
        self.assertEqual(self.animal.status, 'd')
        self.assertEqual(self.animal.adopter_first_name, 'John')
        self.assertEqual(self.animal.adopter_last_name, 'Doe')

    def test_create_cage_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('cage_create')
        data = {
            'room': 'Side Room',
            'cage': 2,
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home_page'))
        self.assertTrue(Building.objects.filter(room='Side Room', cage=2).exists())

    def test_create_allergy_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('allergy_create')
        data = {
            'allergy': 'Peanuts',
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('allergy_list'))
        self.assertTrue(Allergies.objects.filter(allergy='Peanuts').exists())

    def test_create_medication_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('medication_create')
        data = {
            'name': 'Ibuprofen',
            'type1': 'p',
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('medication_list'))
        self.assertTrue(Medication.objects.filter(name='Ibuprofen').exists())

    def test_delete_animal_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('animal_instance_delete', kwargs={'pk': self.animal.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('home_page'))
        self.assertFalse(AnimalInstance.objects.filter(pk=self.animal.pk).exists())

    def test_delete_cage_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('cage_delete', kwargs={'pk': self.building.pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse('home_page'))
        self.assertFalse(Building.objects.filter(pk=self.building.pk).exists())

    def test_update_animal_post(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('animal_instance_update', kwargs={'pk': self.animal.pk})
        current_date = timezone.now()
        data = {
            'name': 'Dexter Updated',
            'animal_species': 'Dog',
            'breed': 'Labrador',
            'status': 'a',
            'arrival_date': current_date,
            'gender': 'm',
            'hair_type': 'f',
            'hair_length': 's',
            'bio': 'Updated bio',
            'cross': False,
            'food_type': 'h',
            'portion_size': 1.0,
            'daily_portions': 2.0
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('home_page'))
        self.animal.refresh_from_db()
        self.assertEqual(self.animal.name, 'Dexter Updated')

class FilterTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.building = Building.objects.create(
           room = 'Main',
           cage = 1,
        )
        current_date = timezone.now()
        # Create animals with different statuses
        self.available_animal = AnimalInstance.objects.create(
            name = 'Available',
            status = 'a',
            arrival_date = current_date,
            gender = 'm',
            cage = self.building,
        )
        self.adopted_animal = AnimalInstance.objects.create(
            name = 'Adopted',
            status = 'd',
            arrival_date = current_date,
            gender = 'f',
            cage = self.building,
        )
        self.quarantine_animal = AnimalInstance.objects.create(
            name = 'Quarantine',
            status = 'q',
            arrival_date = current_date,
            gender = 'm',
            cage = self.building,
        )

    def test_available_animals_filter(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('available_animals')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['animal_instances_available']), 1)
        self.assertEqual(response.context['animal_instances_available'][0], self.available_animal)

    def test_adopted_animals_filter(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('adopted_animals')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['animal_instances_adopted']), 1)
        self.assertEqual(response.context['animal_instances_adopted'][0], self.adopted_animal)

    def test_quarantine_animals_filter(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        url = reverse('quarantined_animals')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['animal_instances_quaratine']), 1)
        self.assertEqual(response.context['animal_instances_quaratine'][0], self.quarantine_animal)


