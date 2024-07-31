from django.urls import path
from .views import profile_user, \
    RegisterUser, UserLogin, UserLogout

app_name = 'app_users'

urlpatterns = [
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    #path('profile/', profile_user, name='profile_user'),
]
