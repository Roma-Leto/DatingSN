from django.urls import path
from .views import login_user, logout_user, profile_user, RegisterUser

app_name = 'app_users'

urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile_user, name='profile_user'),
]
