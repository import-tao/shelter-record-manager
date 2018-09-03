from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect
from .forms import SignUpForm, CustomEditProfileForm

from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
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
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def userProfileView(request):
    user = request.user
    context = {
        'user': user,
            }
    return render(request, 'accounts/user_profile.html', context)

@login_required
def userEditView(request):
    if request.method == 'POST':
        form = CustomEditProfileForm(data=request.POST, instance= request.user)
        if form.is_valid:
            form.save()
            return redirect('user_profile')
    else:
        form = CustomEditProfileForm(instance = request.user)
        context = {
            'form':form
        }
        return render(request, 'accounts/user_edit.html', context)

