"""airlinedb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from airlineApp import views

# Importing views from the current directory

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.showindex, name='showindex'),
    url('admin_home', views.admin_home, name='admin_home'),
    url('user_home', views.user_home, name='user_home'),
    url('logcheck', views.logcheck, name='logcheck'),
    url('changepass', views.changepass, name='changepass'),

    # Employee Details URLs
    url('insertemployee_details', views.insertemployee_details, name='insertemployee_details'),
    url('employee_detailsview', views.employee_detailsview, name='employee_detailsview'),

    # Shop Details URLs
    url('insertshop_details', views.insertshop_details, name='insertshop_details'),
    url('shop_detailsview', views.shop_detailsview, name='shop_detailsview'),

    # Complaints URLs
    url('insertcomplaints', views.insertcomplaints, name='insertcomplaints'),
    url('complaintsview', views.complaintsview, name='complaintsview'),

    # Service Details URLs
    url('insertservicedetails', views.insertservicedetails, name='insertservicedetails'),
    url('servicedetailsview', views.servicedetailsview, name='servicedetailsview'),

    # Incharge Details URLs
    url('insertincharge_details', views.insertincharge_details, name='insertincharge_details'),
    url('incharge_detailsview', views.incharge_detailsview, name='incharge_detailsview'),

    # Food Store URLs
    url('insertFood_store', views.insertFood_store, name='insertFood_store'),
    url('Food_storeview', views.Food_storeview, name='Food_storeview'),

    # Register URLs
    url('insertRegister', views.insertRegister, name='insertRegister'),
    url('Registerview', views.Registerview, name='Registerview'),
]

