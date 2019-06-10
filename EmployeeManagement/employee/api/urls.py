from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = "employees-api"

urlpatterns = [
    path('create/', views.EmployeeCreateAPIView.as_view(), name='create'),
    path('list/',views.EmployeeListAPIView.as_view(),name="list"),
    path('detail/<pk>/',views.EmployeeDetailAPIView.as_view(),name="list"),
    path('detail/<pk>/update/',views.EmployeeDetailUpdateAPIView.as_view(),name="update"),
    path('detail/<pk>/delete/',views.EmployeeDeleteAPIView.as_view(),name="delete"),
    #path('login/', views.UserLoginAPIView.as_view(), name='login'),


    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]