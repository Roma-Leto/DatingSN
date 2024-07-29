from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterUserForm


def login_user(request):
    return HttpResponse("Login")


def logout_user(request):
    return HttpResponse("Logout")


def profile_user(request):
    return HttpResponse("Profile")


# def register(request):
#     form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('app_social:homepage')

