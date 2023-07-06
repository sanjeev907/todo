from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','address']

admin.site.register(Todo,TodoAdmin)