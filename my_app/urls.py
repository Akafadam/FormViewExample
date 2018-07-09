from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('login/', auth_views.login, {'template_name': 'my_app/login.html'}, name='signin'),
	path('profile/', views.HomeView.as_view(template_name='my_app/home.html'), name='home')
]