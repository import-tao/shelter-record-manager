from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Your name', max_length= 30)
    email = forms.EmailField()
    subject = forms.CharField(max_length= 20,)
    text = forms.CharField(widget=forms.Textarea)
    ccmyself = forms.BooleanField(required=False)