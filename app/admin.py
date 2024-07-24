from django.contrib import admin
from .models import *
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','address']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','address','phone']
    
admin.site.register(Todo,TodoAdmin)
admin.site.register(User)
admin.site.register(Todo1)