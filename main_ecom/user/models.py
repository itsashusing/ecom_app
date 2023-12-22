from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BillingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=20)
    city=models.CharField(max_length=50)


    def __str__(self):
        return f'{self.user}'