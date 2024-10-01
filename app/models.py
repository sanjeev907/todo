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

    def __str__(self):
        return self.name

class Todo1(models.Model):
    Name = models.CharField(max_length=50)

class TodoTask(models.Model):
    name = models.CharField(max_length=50)
    task = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    address_status = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

