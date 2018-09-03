from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class PageResponse(TestCase):
    
    def url_redirect_tests(self, url, template_name='registration/login.html', redirect='/accounts/login/?next=/accounts/profile/'):
        response = self.client.get(url, follow=True)
        self.assertRedirects(response, redirect)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name)
        return response

    def test_accounts_profile_view_status_code(self):
        url = reverse('user_profile')
        self.url_redirect_tests(url)
        

    def test_accounts_profile_edit_view_status_code(self):
        url = reverse('user_profile_edit')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/accounts/profile/edit/')

    def test_accounts_password_update_view_status_code(self):
        url = reverse('password_update')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/accounts/profile/password/')


    def test_accounts_signup_view_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed('/accounts/login.html')
        self.assertTemplateUsed('/accounts/signup.html')

    def test_accounts_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/accounts/login.html')

    def test_accounts_logout_view_status_code(self):
        url = reverse('logout')
        self.url_redirect_tests(url, 'index/index.html', '/')
        

    def test_accounts_password_change_done_view_status_code(self):
        url = reverse('password_change_done')
        self.url_redirect_tests(url, redirect='/accounts/login/?next=/accounts/password_change/done/')

    def test_accounts_password_reset_view_status_code(self):
        url = reverse('password_reset')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/accounts/password_reset.html')

    def test_accounts_password_reset_done_view_status_code(self):
        url = reverse('password_reset_done')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/accounts/password_reset_done.html')

    def test_accounts_password_reset_complete_view_status_code(self):
        url = reverse('password_reset_complete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('/accounts/password_reset_complete.html')


class LoggedinResponse(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK') 
        test_user1.save()

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
    
    def test_accounts_profile(self):
        url = reverse('user_profile')
        template = 'accounts/user_profile.html'
        self.login_testing(url, template)
    
    def test_accounts_profile_edit(self):
        url = reverse('user_profile_edit')
        template = 'accounts/user_edit.html'
        self.login_testing(url, template)
    