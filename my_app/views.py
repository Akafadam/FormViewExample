from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm
from django.contrib.auth.forms import User

class ContactView(FormView):
	form_class = LoginForm
	success_url = '/thanks/'
	template_name = 'my_app/index.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username=username, email=email, 
		password=password)
		
		return super(ContactView, self).form_valid(form)