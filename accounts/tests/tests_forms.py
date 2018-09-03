from django.test import TestCase
from django.contrib.auth.models import User

from accounts.forms import SignUpForm
from accounts.models import PermittedEmails

class SignUpTest(TestCase):
    def setUp(self):
        PermittedEmails.objects.create(
            email='test@gmail.com'
        )
        PermittedEmails.objects.create(
            email='youcansignup@gmail.com'
        )

        User.objects.create(
            username = "Tester",
            first_name= "Testfirstname",
            last_name= "Testsurname",
            email = "test@gmail.com",
            password= "ThisistheT3stpassw0rd",
        )
        '''
    def test_sign_up(self):
        form = SignUpForm(data={
            'username':'test1',
        })
        self.assertTrue(form.is_valid())
    '''
    def test_valid_sign_up(self):
        form = SignUpForm(data={
            'username':'test1',
            'first_name':'firstname',
            'last_name':'secondname',
            'email':'youcansignup@gmail.com',
            'password1':'Asuperduperstrongpassword',
            'password2':'Asuperduperstrongpassword',
        })
        self.assertTrue(form.is_valid())
    
    def test_email_not_permitted_sign_up(self):
        form = SignUpForm(data={
            'username':'test1',
            'first_name':'firstname',
            'last_name':'secondname',
            'email':'wrong@gmail.com',
            'password1':'Asuperduperstrongpassword',
            'password2':'Asuperduperstrongpassword',
        })
        self.assertFalse(form.is_valid())
    
    def test_email_already_used_sign_up(self):
        form = SignUpForm(data={
            'username':'test1',
            'first_name':'firstname',
            'last_name':'secondname',
            'email':'test@gmail.com',
            'password1':'Asuperduperstrongpassword',
            'password2':'Asuperduperstrongpassword',
        })
        self.assertFalse(form.is_valid())

    def test_username_already_used_sign_up(self):
        form = SignUpForm(data={
            'username':'Tester',
            'first_name':'firstname',
            'last_name':'secondname',
            'email':'youcansignup@gmail.com',
            'password1':'Asuperduperstrongpassword',
            'password2':'Asuperduperstrongpassword',
        })
        self.assertFalse(form.is_valid())