from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import User, UserCreationForm

class ContactView(FormView):
	form_class = LoginForm
	success_url = '/thanks/'
	template_name = 'my_app/index.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, email=email, password=password)
		login(request, user)
		return super(ContactView, self).form_valid(form)