"""FindShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include,path
from FindShopApp import views

app_name = 'FindShopApp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.MyIndexView.as_view(),name="my_index_view"),
    path('index Customer',views.MyIndexViewCustomer.as_view(),name="my_index_view_Customer"),
    path('landing',views.MyLandingView.as_view(),name="my_landing_view"),
    path('registrationAdmin',views.MyAdminRegistrationView.as_view(),name="my_adminregistration_view"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.login,name="login"),
    path('login Admin',views.loginAdmin,name="loginAdmin"),
    path('register',views.register,name="register"),
]
