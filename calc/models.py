from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Usermedia(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=10, blank=True)
    Password = models.CharField(max_length=100, blank=True)


