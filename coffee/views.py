from django.shortcuts import render, redirect
from .forms import SignUp, Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def usersignup(request):
	context = {}
	form = SignUp()
	context['form'] = form
	if request.method == 'POST':
		form = SignUp(request.POST)
		if form.is_valid():
			user = form.save()
			username = user.username
			password = user.password

			user.set_password(password)
			user.save()

			authUser = authenticate(username=username, password=password)
			login(request, authUser)

			return redirect('coffee:list') #list
		messages.error(request, form.errors)
		return redirect('coffee:signup')
	return render(request,'signup.html', context)

def userlogin(request):
	context = {}
	form = Login()
	context['form'] = form
	if request.method == 'POST':
		form = Login(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			authUser = authenticate(username=username, password=password)
			if authUser is not None:
				login(request, authUser)
				return redirect('coffee:list') #list

			messages.warning(request, 'Wrong Username/Password. Please Try Again.')
			return redirect('coffee:login')
	return render(request,'login.html', context)

def logout(request):
	logout(request)
	return redirect('coffee:login')


def list(request):
	return HttpResponse()