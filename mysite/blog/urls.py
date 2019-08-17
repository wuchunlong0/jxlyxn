# -*- coding: utf-8 -*-
from django.conf.urls import url, include
#from django.urls import path
from . import views

urlpatterns = [
    url(r'index0/', views.index0, name="index0"),
    url(r'index/', views.index, name="index"),
    url(r'company/', views.company, name="company"),    
    url(r'device/', views.device, name="device"), 
    url(r'testing/', views.testing, name="testing"), 
    url(r'contactus/', views.contactus, name="contactus"), 
    url(r'contact/list/(\d*)?$', views.contact_list, name='contact_list'),
    url(r'contact/edit/', views.contact_edit, name="contact_edit"),
    url(r'customer/', views.customer, name="customer"),  
    url(r'product/profile/', views.product_profile, name="product_profile"),
    url(r'product/', views.product, name="product"),
    url(r'Journalism/', views.Journalism, name="Journalism"),  


]
