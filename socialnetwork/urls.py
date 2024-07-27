from django.urls import path
from .views import index

app_name = 'app_social'

urlpatterns = [
    path('', index, name="homepage"),
]
