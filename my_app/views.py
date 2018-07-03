from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from .forms import LoginForm
import imaplib

class ContactView(FormView):
	form_class = UserCreationForm
	success_url = '/thanks/'
	template_name = 'my_app/index.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		# server = imaplib.IMAP4_SSL('imap.gmail.com')
		# server.login(email, password)
		user = authenticate(username=username, password=password)
		login(request, user)

		return super(ContactView, self).form_valid(form)