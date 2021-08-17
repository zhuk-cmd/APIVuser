from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import  Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
from app_1.models import Employee
from app_1.serializer import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet




class APIVall_data(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# class APIVuser(ModelViewSet):
#     queryset = Employee.objects.filter(id)
#     serializer_class = EmployeeSerializer