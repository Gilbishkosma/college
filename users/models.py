from django.db import models
import random
import string
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.


class CustomUser(AbstractUser):
	College = models.CharField(max_length=100)

	def __str__(self):
	    return self.username
        
class Token(models.Model):
    key=models.CharField(max_length=40,unique=True)
    user=models.OneToOneField(CustomUser,related_name='auth_token',on_delete=models.CASCADE, verbose_name="user",unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def generate_key(self):
        return ''.join(random.choice(string.ascii_lowercase+string.digits+string.ascii_uppercase) for i in range(40))

    def save(self,*args,**kwargs):
        if not getattr(self,'key',None):
            new_key=self.generate_key()
            while type(self).objects.filter(key=new_key).exists():
                new_key=self.generate_key()
            self.key=new_key
        return super(Token,self).save(*args,**kwargs)

