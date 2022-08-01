from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        return []


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
