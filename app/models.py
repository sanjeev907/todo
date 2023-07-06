from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address = models.CharField(max_length=100)

