from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import User, UserCreationForm

class SignUpView(FormView):
	form_class = UserCreationForm
	success_url = '/thanks/'
	template_name = 'myapp/signup.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		login(self.request, user)

		return super(SignUpView, self).form_valid(form)