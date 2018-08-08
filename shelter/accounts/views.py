from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    # prevents a logged in user to see sign up page
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        if User.is_authenticated:
            return render(request, 'index/index.html')
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

@login_required
def userProfileView(request, pk):
    user = User.objects.get(pk=pk)
    if request.user.pk == pk
    context = {
        'user': user,
            }
    return render(request, 'registration/user_profile.html', context)




