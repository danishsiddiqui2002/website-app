from django.contrib import admin
from django.urls import path
from Nanoapp import views

urlpatterns = [
  path("", views.index, name='home'),
  path("services/", views.services, name='services'),
  path("lms/", views.lms, name='lms'),
  path("blog/", views.blog, name='blog'),
  path("contact/", views.contact, name='contact'),
  path("about/", views.about, name='about'),
  path("service1/", views.service1, name='service1'),
  path("service2/", views.service2, name='service2'),
  path("service3/", views.service3, name='service3'),
  path("service4/", views.service4, name='service4'),
  path("service5/", views.service5, name='service5'),
  path("service6/", views.service6, name='service6'),
  path("service7/", views.service7, name='service7'),
  path("service8/", views.service8, name='service8'),
  path("service9/", views.service9, name='service9'),
  path("announcement/", views.announcement, name='announcement'),
  ]