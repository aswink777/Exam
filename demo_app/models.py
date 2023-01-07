from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Login(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Trainer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='trainer', null=True, blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    qualification = models.CharField(max_length=50)
    achievement = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pic')


