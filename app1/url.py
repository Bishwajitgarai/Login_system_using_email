from os import name
from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.index,name="Index"),
    path('check', views.check,name="email"),
    path('verify', views.verify,name="otp"),
    path('login_page', views.login_page,name="login"),
    path('login_check', views.login_check,name="login_check"),
    path('sign_up_page', views.sign_up_page,name="login"),
    path('login_out', views.login_out,name="loginout"),
    
]