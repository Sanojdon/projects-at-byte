from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
	path('', views.index, name='index'),
	path('details/', views.details, name='details'),
]
