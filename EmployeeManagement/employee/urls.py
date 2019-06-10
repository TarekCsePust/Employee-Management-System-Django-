from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name="employee"
urlpatterns = [
    path('create/',views.CreateEmployee,name="create"),
    path('',views.EmployeeList,name="list"),
    path('<pk>/details',views.EmployeeDetail,name="detail"),
    path('<pk>/details/update',views.EmployeeUpdate,name="update"),
]
