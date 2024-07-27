from django.http import HttpResponse
from django.shortcuts import render

from users.forms import RegisterUserForm


def login_user(request):
    return HttpResponse("Login")


def logout_user(request):
    return HttpResponse("Logout")


def profile_user(request):
    return HttpResponse("Profile")


def register(request):
    form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})
