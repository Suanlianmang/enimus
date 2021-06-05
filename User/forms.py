from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from .models import CHOICE, Profile

class UserLoginForm(forms.ModelForm):
	phone_number = PhoneNumberField(widget=forms.TextInput(attrs={}), label='Phone number')
	class Meta:
		model = User
		fields = ['phone_number', 'password']

class UserRegisterForm(forms.ModelForm):
	phone_number = PhoneNumberField(widget=forms.TextInput(attrs={}), label='Phone number')
	user_type = forms.ChoiceField(choices=CHOICE)
	class Meta:
		model = Profile
		fields = ['phone_number', 'user_type']