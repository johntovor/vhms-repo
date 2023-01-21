from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .models import SystemAdministrator, Client
from .forms import (ClientForm, LoginForm, UserUpdateForm,
                    ClientProfileUpdateForm, AdministratorForm)

User = settings.AUTH_USER_MODEL

"""begin:: client registration view"""


def register_admin(request):
    template_name = 'accounts/register-admin.html'
    if request.method == 'POST':
        admin_register_form = AdministratorForm(request.POST)

        if admin_register_form.is_valid():
            user = admin_register_form.save()

            # if 'profile_pic' in request.FILES:
            #     user.profile_pic = request.FILES['profile_pic']
            user.save()
            messages.success(
                request, 'Congratulations! Your account has been created successfully.')
            return redirect('accounts:signin')
    else:
        admin_register_form = AdministratorForm()

    context = {
        'admin_register_form': admin_register_form,
    }

    return render(request, template_name, context)


def register_client(request):
    template_name = 'accounts/register-client.html'
    if request.method == 'POST':
        client_register_form = ClientForm(request.POST)

        if client_register_form.is_valid():
            user = client_register_form.save()

            # if 'profile_pic' in request.FILES:
            #     user.profile_pic = request.FILES['profile_pic']
            user.save()
            messages.success(
                request, 'Congratulations! Your account has been created successfully.')
            return redirect('accounts:signin')
    else:
        client_register_form = ClientForm()

    context = {
        'client_register_form': client_register_form,
    }

    return render(request, template_name, context)


"""end:: client registration view"""


"""begin:: user login view"""


def signin(request):
    template_name = 'accounts/login.html'
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():

            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('dashboard:dashboard')

    else:
        login_form = LoginForm()

    context = {
        'login_form': login_form
    }

    return render(request, template_name, context)


"""end:: user login view"""


"""begin:: user logout view"""


@login_required(login_url='accounts:signin')
def signout(request):
    logout(request)

    messages.success(request, 'You have logged out successfully!')
    return redirect('core:index')


"""end:: user logout view"""


"""User Profile"""


@login_required(login_url='accounts:signin')
def admin_profile(request):
    template_name = 'accounts/admin-profile.html'

    admin_profile = SystemAdministrator.objects.get(user=request.user)

    context = {
        'admin_profile': admin_profile,
    }

    return render(request, template_name, context)


@login_required(login_url='accounts:signin')
def client_profile(request):
    template_name = 'accounts/client-profile.html'

    client_profile = Client.objects.get(user=request.user)

    context = {
        'client_profile': client_profile,
    }

    return render(request, template_name, context)


"""User Profile"""
