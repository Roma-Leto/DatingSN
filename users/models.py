from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,
                              null=True, verbose_name="Фотография")
    date_birth = models.DateTimeField(verbose_name="Дата рождения")
    about_me = models.CharField(max_length=500, blank=True, null=True)
