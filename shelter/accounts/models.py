from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
'''
class User(AbstractBaseUser):
    email = models.EmailField(max_length= 255, unique=True, verbose_name='email address')
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    def __str__(self):
        return


    @property
    def get_full_name(self):
        return self.first_name + self.last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def last_login(self):
        return self.last_login

    '''