from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  # tc = models.CharField(max_length=20) username kullanılacak
  adres = models.CharField(max_length=250)
  ilce = models.CharField(max_length=30)
  il = models.CharField(max_length=20)
  ülke = models.CharField(max_length=20)
  telefon = models.CharField(max_length=15)
