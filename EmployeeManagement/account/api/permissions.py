from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
    )
from django.contrib.auth import get_user_model
from django.shortcuts import reverse,render,get_object_or_404
User = get_user_model()

def IsWoner(self,*args,**kwargs):
    token = self.request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        #print(token)
    data = {'token': token}
        
    valid_data = VerifyJSONWebTokenSerializer().validate(data)
    user = valid_data['user']
    is_Woner = get_object_or_404(User,pk=self.kwargs['pk'])
    tmp1 = str(is_Woner.username)
    tmp2 = str(user)
    if(tmp1 != tmp2):
        return False
    return True