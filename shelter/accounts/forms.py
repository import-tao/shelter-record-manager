from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model= User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class CustomEditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
