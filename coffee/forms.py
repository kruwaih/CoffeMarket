from django.contrib.auth.models import User
from django import forms

class SignUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

		widgets = {
		'password': forms.PasswordInput(),
		}

class Login(forms.Form):
		username = forms.CharField(required=True)
		password = forms.CharField(required=True, widget=forms.PasswordInput())