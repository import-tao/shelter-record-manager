from datetime import datetime

from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from ..models import AnimalInstance, Building, Allergies, Medication
from ..views import homepage_view
# Create your tests here.

class PageRedirectstoLogin(TestCase):
    ''' Check the url redirects to login page when not logged in,
    and the correct next page.
    '''
    def setUp(self):
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
    ''' Check a logged in user gets to the correct page
    '''
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK') 
        test_user1.save()

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


    def login_testing(self, url, template, content=""):
        ''' Check logged in user accesses correct template and checks content.
        '''
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # dont use follow as the request should not be redirected (302)
        response = self.client.get(url)
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, template)
        self.assertContains(response, content)

    def test_homeview_logged_in_user(self):
        url = reverse('home_page')
        template = 'catalog/homepage.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_adopted_animals(self):
        url = reverse('adopted_animals')
        template = 'catalog/adopted_animals.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_create_view(self):
        url = reverse('animal_create')
        template = 'catalog/animalcreate.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_detail(self):
        url = reverse('animal_detail',kwargs= {'pk':1})
        template = 'catalog/animaldetail.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_instance_update(self):
        url = reverse('animal_instance_update',kwargs= {'pk':1})
        template = 'catalog/animal_instance_update.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_instance_delete(self):
        url = reverse('animal_instance_delete',kwargs= {'pk':1})
        template = 'catalog/animal_instance_delete.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_adopt_new(self):
        url = reverse('adopt_new',kwargs= {'pk':1})
        template = 'catalog/adopt_animal.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_animal_adopt_existing(self):
        url = reverse('adopt_existing',kwargs= {'pk':1})
        template = 'catalog/adopted_animal_update.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_cage_detail(self):
        url = reverse('cage_detail')
        template =  'catalog/cage_detail.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_cage_create(self):
        url = reverse('cage_create')
        template =  'catalog/cage_create.html'
        content = ''
        self.login_testing(url, template, content)
    
    def test_app_cage_update(self):
        url = reverse('cage_update', kwargs={'pk':1})
        template =  'catalog/cage_update.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_cage_delete(self):
        url = reverse('cage_delete', kwargs={'pk':1})
        template =  'catalog/cage_delete.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_allergy_list(self):
        url = reverse('allergy_list')
        template =  'catalog/allergies_list.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_allergy_create(self):
        url = reverse('allergy_create')
        template =  'catalog/allergy_create.html'
        content = ''
        self.login_testing(url, template, content)


    def test_app_allergy_delete(self):
        url = reverse('allergy_delete', kwargs={'pk':1})
        template =  'catalog/allergy_delete.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_medication_list(self):
        url = reverse('medication_list')
        template =  'catalog/medication_list.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_medication_create(self):
        url = reverse('medication_create')
        template =  'catalog/medication_create.html'
        content = ''
        self.login_testing(url, template, content)

    def test_app_medication_delete(self):
        url = reverse('medication_delete', kwargs={'pk':1})
        template =  'catalog/medication_delete.html'
        content = ''
        self.login_testing(url, template, content)