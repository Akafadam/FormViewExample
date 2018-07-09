from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import SignUpForm
from django.contrib.auth import login, authenticate

class SignUpView(FormView):
	form_class = SignUpForm
	success_url = '/thanks/'
	template_name = 'myapp/signup.html'

	def form_valid(self, form):
		form.save()
		username = form.cleaned_data['username']
		password = form.cleaned_data['password1']
		user = authenticate(username=username, password=password)
		login(self.request, user)

		return super(SignUpView, self).form_valid(form)

class HomeView(TemplateView):

	def get(self, request):
		return render(request, self.template_name)