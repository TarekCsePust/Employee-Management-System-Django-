from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = "users-api"

urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('detail/<pk>', views.UserDetailAPIView.as_view(), name='detail'),
    path('detail/<pk>/update', views.UserDetailUpdateAPIView.as_view(), name='detail'),
    path('jwt/api-token-auth/', obtain_jwt_token, name='obtain_jwt_token'),
    #path('login/', views.UserLoginAPIView.as_view(), name='login'),


    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]