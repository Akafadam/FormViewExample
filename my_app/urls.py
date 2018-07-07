from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('login/', auth_views.login, {'template_name': 'myapp/login.html'}, name='signin'),
]