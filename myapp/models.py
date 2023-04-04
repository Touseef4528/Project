from django.db import models

# Create your models here.

class login_user(models.Model):

    email = models.CharField(max_length=30) 
    password = models.CharField(max_length=30)


class registration_user(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
