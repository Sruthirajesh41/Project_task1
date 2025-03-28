"""
URL configuration for Login_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from login_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration',views.user_registration,name='registration'),
    path('',views.home),
    path('login',views.LoginUser,name='login'),
    path('user_home',views.user_home,name='user_home'),
    path('add_mark',views.add_mark,name='add_mark'),
    path('logout',views.LogoutUser,name='logout'),
    path('mark_details',views.MarkDetails,name='mark_details'),
    path('edit_mark',views.Editmark,name='edit_mark'),
    path('password_reset_request',views.password_reset_request,name='password_reset_request'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('set_new_password',views.set_new_password,name="set_new_password"),
]
