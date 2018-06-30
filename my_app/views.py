from django.shortcuts import render
from django.views.generic import FormView
from .forms import LoginForm

class ContactView(FormView):
	form_class = LoginForm
	success_url = '/thanks/'
	template_name = 'my_app/index.html'

	def form_valid(self, form):
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		return super(ContactView, self).form_valid(form)