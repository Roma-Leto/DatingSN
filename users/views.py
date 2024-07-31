from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterUserForm, UserLoginForm


# def login_user(request):
#     return HttpResponse("Login")


def logout_user(request):
    return HttpResponse("Logout")


def profile_user(request):
    return render(request, "users/profile.html", {'title': 'Профиль'})


# def register(request):
#     form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('app_social:homepage')


class UserLogin(LoginView):
    form_class = UserLoginForm      # AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}

    # Переопределение функции перенаправления после успешной авторизации.
    # По умолчанию - profile
    def get_success_url(self):
        return reverse_lazy("app_users:profile_user")


class UserLogout(LogoutView):
    pass
