from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect,reverse
from rest_framework import serializers
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
    )
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from employee.models import Employee
User = get_user_model()


class EmployeeCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Employee
        fields = [
        	'name',
            'post',    
            'address',
            
            'mobile_no',
            'image',

        ]

    def validate(self, data):
    	return data

    

""" def create(self,request,data):
        
        Create and return a new `Snippet` instance, given the validated data.
        
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        #print(token)
        data = {'token': token}
        
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        username = valid_data['user']
        user= get_object_or_404(User,username=username)
        instance = Employee.objects.create(
            company=user,
        	name=data.get('name'),
        	post=data.get('post'),
        	address=data.get('address'),
            birthdate=datetime.now(),
            mobile_no=data.get('mobile_no'),
            image=data.get('image')
        )
        
        instance.save()

        return instance

"""


class EmployeeListSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'company',
            'name',
            
            
            
        ]

class EmployeeDetailSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'company',
            'name',
            'post',
            'address',
            'mobile_no',
            'birthdate',
            'status',
            
            
        ]

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
        	'id',
        	'first_name',
        	'last_name',
            'username',
            'email',
            
            
        ]

class UserDetailUpdateSerializer(ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = [
            
            'first_name',
            'last_name',
            'password',
            
            
        ]

    def update(self, instance, data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        #instance.password = data.get('is_staff', instance.is_staff)
        #instance.is_superuser = data.get('is_superuser', instance.is_staff)
        instance.set_password(data.get('password'))
        instance.save()
        return instance 

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False,allow_blank=True)
    password = CharField(required=False,allow_blank=True)

    class Meta:
        model = User
        fields = [
            'username',
            
            'password',
            'token'
            

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        username = data.get("username",None)
        password = data.get("password",None)
        if not username or not password:
            raise ValidationError("A username or email is required to login")
        user  = get_object_or_404(User,username=username)
        if user:
            if not user.check_password(password):
                raise  ValidationError("Incorrect credential please try again")
        
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        
        return data


class EmployeeDetailUpdateSerializer(ModelSerializer):
    
    class Meta:
        model = Employee
        fields = [
            'name',
            'post',    
            'address',
            
            'mobile_no',
            'image',
            'status',

        ]

    def validate(self, data):
        return data
    

