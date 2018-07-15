from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import ContactUsForm
from secret_environment_keys import Config

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'index/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            subject = '****EMAIL FROM USER ****' + form.cleaned_data['subject']
            message = form.cleaned_data['text']

            recipients = [Config.EMAIL_HOST_USER]
            if cc_myself:
                recipients.append(sender)
            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect(reverse('index'))
    else:
        form = ContactUs()
        return render(request, 'index/contactus.html',{'form': form})