from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import UserLoginForm, UserRegisterForm


def sign_in(request, key, password, context):
	context ={
	'form': UserLoginForm(),
	'test': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
	'alert': "Your phone number or password is wrong!"
	}
	try:
		profile = Profile.objects.get(phone_number=key)
		username = profile.user.username
		user = authenticate(request, username=username, password=password)
	except:
		return render(request, 'User/index.html', context)
	if user is not None:
		login(request,user)
		return render(request, 'test.html', context)

def main(request):
	context ={
	'form': UserLoginForm(),
	'test': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	}
	if request.method == 'GET':
		logout(request)
		return render(request, 'User/index.html', context)
	if request.POST.get('signin', '') == 'signin':
		form = request.POST
		key = form.get('phone_number', '')	
		password = form.get('password', '')	
		return sign_in(request, key, password, context)


	return render(request, 'User/index.html', context)



def customer_signup(request):
	context = {
		'form': UserLoginForm(),
		'form1': UserRegisterForm(),
		'form2': UserCreationForm(),
	}
	if request.method == 'POST':
		if request.POST.get('signup', '') == 'signup':
			phone_number = request.POST.get('phone_number', '')
			check = Profile.objects.filter(phone_number=phone_number)
			if check.count() != 0:
				context = {	
				'form': UserLoginForm(),
				'form1': UserRegisterForm(),
				'form2': UserCreationForm(),
				'alert': "User with the number already exist!!"
				}
				return render(request, 'User/customer_signup.html', context)
			form = UserCreationForm(request.POST)
			if form.is_valid():
				form.save()
				username = form.cleaned_data['username']
				password = form.cleaned_data['password1']
				user = authenticate(username = username,password = password)
				login(request, user)
				user = User.objects.get(username=username)
				form = request.POST
				user.profile.phone_number = form.get('phone_number', '')
				user.profile.user_type = form.get('user_type', '')
				user.save()
				return render(request, 'User/index.html')
			else:
				context = {
				'form': UserLoginForm(),
				'form1': UserRegisterForm(),
				'form2': UserCreationForm(),
				'alert': "Username already exist!"
				}

				return render(request, 'User/customer_signup.html', context)
		elif request.POST.get('signin', '') == 'signin':
			form = request.POST
			key = form.get('phone_number', '')	
			password = form.get('password', '')	
			return sign_in(request, key, password, context)
	return render(request, 'User/customer_signup.html', context)

def seller_signup(request):
	context = {
	'form1': UserRegisterForm(),
	'form2': UserCreationForm(),
	}
	return render(request, 'User/seller_signup.html', context)