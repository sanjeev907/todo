from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

class Todo1(models.Model):
    Name = models.CharField(max_length=50)

