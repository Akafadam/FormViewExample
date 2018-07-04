from django import forms

class LoginForm(forms.Form):
	name = forms.CharField()
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_pwd = forms.CharField(widget=forms.PasswordInput())