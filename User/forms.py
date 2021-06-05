from django import forms
from django.contrib.auth.models import User
from .models import CHOICE, Profile

class UserLoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['phone_number', 'password']

class UserRegisterForm(forms.ModelForm):
	user_type = forms.ChoiceField(choices=CHOICE)
	class Meta:
		model = Profile
		fields = ['phone_number', 'user_type']
