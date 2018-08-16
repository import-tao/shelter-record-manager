from django.test import TestCase
from django.urls import reverse
# Create your tests here.


class PageResponse(TestCase):
    def test_accounts_profile_view_status_code(self):
        url = reverse('user_profile')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_profile_edit_view_status_code(self):
        url = reverse('user_profile_edit')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_update_view_status_code(self):
        url = reverse('password_update')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_signup_view_status_code(self):
        url = reverse('signup')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_login_view_status_code(self):
        url = reverse('login')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_logout_view_status_code(self):
        url = reverse('logout')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_change_view_status_code(self):
        url = reverse('password_change')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_change_done_view_status_code(self):
        url = reverse('password_change_done')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_reset_view_status_code(self):
        url = reverse('password_reset')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_reset_done_view_status_code(self):
        url = reverse('password_reset_done')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)

    def test_accounts_password_reset_complete_view_status_code(self):
        url = reverse('password_reset_complete')
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 200)