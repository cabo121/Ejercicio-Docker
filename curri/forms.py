from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import curriculum,info
from django.contrib.auth.models import User


class CustomUserForm (UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class curriForm (forms.ModelForm):
	
	class Meta:
		model = curriculum
		fields = '__all__'

class infoForm (forms.ModelForm):
	
	class Meta:
		model = info
		fields = '__all__'
