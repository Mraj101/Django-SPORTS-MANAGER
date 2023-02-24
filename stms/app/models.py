from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password = models.CharField(max_length=30)

