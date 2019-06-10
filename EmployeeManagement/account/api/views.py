from django.db.models import Q
from django.contrib.auth import get_user_model
import json
from django.shortcuts import reverse,render,get_object_or_404

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
from .permissions import IsWoner
import requests 






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
    UserCreateSerializer,
    UserDetailSerializer,
    UserDetailUpdateSerializer,
    UserLoginSerializer,

    
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    
    def check_object_permissions(self, request, obj):
        if(not IsWoner(self,self.args,self.kwargs)):
            self.permission_denied(request)

    

        
class UserDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserDetailUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def check_object_permissions(self, request, obj):
        if(not IsWoner(self,self.args,self.kwargs)):
            self.permission_denied(request)   


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data



        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            response_login = requests.post(
            request.build_absolute_uri(reverse('users-api:obtain_jwt_token')),
            data=data
            )
            print(response_login.content)
            response_login_dict = json.loads(response_login.content)
            return Response(response_login_dict, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

