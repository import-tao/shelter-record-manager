from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactUsForm
from .settings.secret_environment_keys import Config
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
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['text']
            cc_myself = form.cleaned_data['cc_myself']
            if cc_myself:
                recipients = [sender]
                send_mail(subject,message,sender,recipients)
            subject = '***CONTACT US FORM *** ' + subject
            recipients = [Config.EMAIL_HOST_USER]
            message = f'PERSON: {name} \nCC SENDER: {cc_myself} \nSUBJECT: {subject}  \nMESSAGE: {message}'
            send_mail(subject, message, sender, recipients)
            messages.success(request, 'Your message was successfully sent!')
            return HttpResponseRedirect(reverse('index'))
        else:
            form = ContactUsForm()
            return render(request, 'index/contactus.html', {'form':form})
    else:
        form = ContactUsForm()
        return render(request, 'index/contactus.html',{'form': form})

