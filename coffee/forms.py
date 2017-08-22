from django.contrib.auth.models import User
from django import forms
from .models import *

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

class CoffeeForm(forms.ModelForm):
	class Meta:
		model = Coffee
		fields = '__all__'
		exclude = ['user', 'price']


class BeansForm(forms.ModelForm):
	class Meta:
		model = Beans
		fields = '__all__'

class SyrupForm(forms.ModelForm):
	class Meta:
		model = Syrup
		fields = '__all__'

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = '__all__'

class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['name']

class CityForm(forms.ModelForm):
	class Meta:
		model=City
		fields=['name']

class AddressForm(forms.ModelForm):
	class Meta:
		model=Address
		fields='__all__'
		exclude = ['user']