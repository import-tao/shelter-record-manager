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
    form_class = ContactUsForm

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