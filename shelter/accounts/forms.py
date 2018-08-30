from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

approved_emails= [
    'smith@gmail.com',
]



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
    
    # Control who signs up by checking their email. Add in a new elseif for permitted people
    # This is only practical for small number of people.
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email in approved_emails:
            raise forms.ValidationError(
                'You are not permitted to sign up. Please contact us using the Contact Us page.'
                )
        return email

class CustomEditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )
