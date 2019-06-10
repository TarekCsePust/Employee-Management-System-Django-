from django.db.models import Q
from django.contrib.auth import get_user_model
import json
from django.shortcuts import reverse,render,get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )
from account.api.permissions import IsWoner
import requests 

from employee.models import Employee




User = get_user_model()

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
    )
from .serializers import (
    EmployeeCreateSerializer,
    EmployeeListSerializer,
    EmployeeDetailSerializer,
    EmployeeDetailUpdateSerializer,
    

    
    )


class EmployeeListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeListSerializer

    def get_queryset(self, *args, **kwargs):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        employees = Employee.objects.filter(company__username=username)
        return employees

class EmployeeDetailAPIView(RetrieveAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated,]

    
    def check_object_permissions(self, request, obj):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        employees = get_object_or_404(Employee,pk=self.kwargs["pk"])
        tmp1 = str(username)
        tmp2 = str(employees.company.username)
        if(tmp1!=tmp2):
            self.permission_denied(request)


            



        
            
class EmployeeCreateAPIView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated,]

    def create(self, request, *args, **kwargs):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        user= get_object_or_404(User,username=username)
        data = request.data
        
        instance = Employee.objects.create(
            company=user,
            name=data.get('name'),
            post=data.get('post'),
            address=data.get('address'),
            mobile_no=data.get('mobile_no'),

        )
        instance.save()
        
        a = {"message":"save data succesfully"}
        return JsonResponse(a)
        
class EmployeeDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = EmployeeDetailUpdateSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def check_object_permissions(self, request, obj):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        employees = get_object_or_404(Employee,pk=self.kwargs["pk"])
        tmp1 = str(username)
        tmp2 = str(employees.company.username)

        if(tmp1!=tmp2):
            self.permission_denied(request)


class EmployeeDeleteAPIView(DestroyAPIView):
    serializer_class = EmployeeDetailSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated,]


    
         

    def check_object_permissions(self, request, obj):
        token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        employees = get_object_or_404(Employee,pk=self.kwargs["pk"])
        tmp1 = str(username)
        tmp2 = str(employees.company.username)
        print("helo......")
        if(tmp1!=tmp2):
            self.permission_denied(
                    request, message="You can not have permission to delete this employee")