from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm
import imaplib

class ContactView(FormView):
	form_class = LoginForm
	success_url = '/thanks/'
	template_name = 'my_app/index.html'

	def form_valid(self, form):
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		server = imaplib.IMAP4_SSL('imap.gmail.com')
		server.login(email, password)
		return super(ContactView, self).form_valid(form)