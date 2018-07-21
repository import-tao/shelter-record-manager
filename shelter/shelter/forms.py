from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(label='Your name',required=True)
    email = forms.EmailField()
    subject = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)