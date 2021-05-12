from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import curriculum,info


class CustomUser (UserCreationForm):
	pass


class curriForm (forms.ModelForm):
	
	class Meta:
		model = curriculum
		fields = '__all__'

class infoForm (forms.ModelForm):
	
	class Meta:
		model = info
		fields = '__all__'