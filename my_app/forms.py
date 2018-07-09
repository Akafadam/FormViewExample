from django import forms
from django.contrib.auth.forms import User, UserCreationForm

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)

