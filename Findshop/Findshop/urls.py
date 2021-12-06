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
    path('indexCustomer',views.MyIndexViewCustomer.as_view(),name="my_index_view_Customer"),
    path('landing',views.MyLandingView.as_view(),name="my_landing_view"),
    path('registrationAdmin',views.MyAdminRegistrationView.as_view(),name="my_adminregistration_view"),
    path('feedback',views.feedback,name="feedback"),
    path('login',views.login,name="login"),
    path('loginAdmin',views.loginAdmin,name="loginAdmin"),
    path('register',views.register,name="register"),
    path('dashboard',views.dashboardView.as_view(),name="dashboard_view"),
    path('reservation',views.reservationView.as_view(),name="reservation_view"),
    path('dashboardmain',views.MyDashboardMainView.as_view(),name="my_dashboard_main_view"),
    path('registration',views.MyProductRegistrationView.as_view(),name="my_productregistration_view"),
    path('dashboardProd',views.MyDashboardView.as_view(),name="my_dashboard_view"),
    path('dashboardReservation', views.MyDashboardReservationView.as_view(), name="my_dashboard_reservation_view"),
    path('dashboardAdmin', views.MyDashboardAdminView.as_view(), name="my_dashboard_admin_view"),
    path('dashboardCustomer',views.MyDashboardCustomerView.as_view(),name="my_dashboard_customer_view"),
    path('product',views.productView.as_view(),name="product"),
    path('shop',views.shopView.as_view(),name="shop"),
]
