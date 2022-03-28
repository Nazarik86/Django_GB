from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='Аватар', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(verbose_name='Город', max_length=36, blank=True)
    phone = models.CharField(verbose_name='Телефон', max_length=20, blank=True)
