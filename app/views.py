from django.shortcuts import render
from .models import *
from .serializers import TodoSerializers, TodoViewSerializers
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import ListAPIView
# Create your views here.

def home(request):
    return HttpResponse("hello world")



class TodoAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoViewSerializers



class TodoView(generics.GenericAPIView):
    def get(self,request):
        data = Todo.objects.all()
        serializers = TodoSerializers(data,many = True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = TodoSerializers(data = request.data)
        if serializers.is_valid():
            Todo.objects.create(name=serializers.data['name'],subject= serializers.data['subject'],email=serializers.data['email'],address= serializers.data['address'])
            return Response(serializers.data)
        
        else:
            return Response(serializers.error_messages)

    def post(self,request,id):
        data1 = Todo.objects.get(id=id)
        serializers = TodoSerializers(data1,data = request.data)
        if serializers.is_valid():
            Todo.objects.update(name=serializers.data['name'],subject= serializers.data['subject'],email=serializers.data['email'],address= serializers.data['address'])
            return Response(serializers.data)
        
        else:
            return Response(serializers.error_messages)
