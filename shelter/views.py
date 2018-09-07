import os

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactUsForm
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def features(request):
    return render(request, 'index/features.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_email = form.cleaned_data['email']
            form_subject = form.cleaned_data['subject']
            form_message = form.cleaned_data['text']
            form_cc_myself = form.cleaned_data['cc_myself']
            if form_cc_myself:
                recipients = [form_email]
                send_mail(form_subject,form_message,form_email,recipients)
            subject = '***CONTACT US FORM *** ' + form_subject
            recipients = [os.environ['ADMINS']]
            message = f'PERSON: {form_name} \nCC SENDER: {form_cc_myself} \nSUBJECT: {form_subject}  \nMESSAGE: {form_message}'
            send_mail(subject, message, form_email, recipients)
            messages.success(request, 'Your message was successfully sent!')
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ContactUsForm()
            return render(request, 'index/contactus.html', {'form':form})
    else:
        form = ContactUsForm()
        return render(request, 'index/contactus.html',{'form': form})

