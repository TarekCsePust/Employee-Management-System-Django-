from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
app_name="account"
urlpatterns = [
   path('login/',views.login_user,name="login"),
   path('logout/',views.logout_user,name="logout"),
   path('profile/',views.getProfile,name="profile"),
   path('profile/update',views.profileUpdate,name="profile_update"),
   path('activate/<uid>/<token>', views.activate, name="activate"),
   path('create/',views.Registration,name="registration"),
   

]
