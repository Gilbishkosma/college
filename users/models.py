from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.


class CustomUser(AbstractUser):
	College = models.CharField(max_length=100)

	def __str__(self):
	    return self.College

