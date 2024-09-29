from rest_framework import serializers
from .models import *

class TodoSerializers(serializers.Serializer):
    name = serializers.CharField(required = True, error_messages={'name':'name is required'})
    subject = serializers.CharField(required = True, error_messages={'subject':'subject is required'})
    email = serializers.CharField(required = True, error_messages={'email':'email is required'})
    address = serializers.CharField(required = True, error_messages={'address':'address is required'})

    