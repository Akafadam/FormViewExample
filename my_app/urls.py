from django.contrib import admin
from django.urls import path, include
from . import views

urlspatterns = [
	path('', views.ContactView.as_view(), name='contact'),
]