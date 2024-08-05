from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, AbstractBaseUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True,
                              null=True, verbose_name="Фотография")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    about_me = models.CharField(max_length=500, blank=True, null=True)

    REQUIRED_FIELDS = ["date_of_birth"]
