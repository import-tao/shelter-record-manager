from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Your name',required=True)
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput())
    subject = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)

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