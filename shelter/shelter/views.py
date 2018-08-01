from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactUsForm, SignUpForm
from secret_environment_keys import Config
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def features(request):
    return render(request, 'index/features.html')

def contact(request):
    form_class = ContactUsForm()

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['text']
            cc_myself = form.cleaned_data['cc_myself']
            if cc_myself:
                recipients = [sender]
                send_mail(subject,message,sender,recipients)
            subject = '***CONTACT US FORM ***' + subject
            recipients = [Config.EMAIL_HOST_USER]
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect(reverse('index'))
        else:
            form = ContactUsForm
            return render(request, 'index/contactus.html', {'form':form})
    else:
        form = ContactUsForm
        return render(request, 'index/contactus.html',{'form': form})

def signup(request):
    # prevents a logged in user to see sign up page
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        #if User.is_authenticated:
         #   return render(request, 'index/index.html')
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})