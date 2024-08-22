from django.contrib import admin
from .models import *

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email','address']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','password','address','phone']

class Todo1Admin(admin.ModelAdmin):
    list_display = ['Name']

class TodoTaskAdmin(admin.ModelAdmin):
    list_display = ['name','task','email','address_status','status','date']
    
admin.site.register(Todo,TodoAdmin)
admin.site.register(User)
admin.site.register(Todo1,Todo1Admin)
admin.site.register(TodoTask,TodoTaskAdmin)