from django.contrib.auth.models import User
from django import forms
from .models import Coffee, Powder, Syrup, Beans, Roast

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
		fields = ['name', 'powder', 'syrup', 'roast', 'beans', 'milk', 'water', 'foam', 'shots', 'extra_instruction']


class BeansForm(forms.ModelForm):
	class Meta:
		model = Beans
		fields = ['name','price']

class SyrupForm(forms.ModelForm):
	class Meta:
		model = Syrup
		fields = ['name', 'price']

class PowderForm(forms.ModelForm):
	class Meta:
		model = Powder
		fields = ['name', 'price']

class RoastForm(forms.ModelForm):
	class Meta:
		model = Roast
		fields = ['name']
