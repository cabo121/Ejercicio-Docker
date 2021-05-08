from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.models import post

#---------------------------------------------------------------

class HomePageView(ListView):
	model = post
	template_name = 'home.html'
	context_object_name = 'docs_list'

class CurriPageView(ListView):
	model = post
	template_name = 'curriculum.html'
	context_object_name = 'docs_list'

class InfoPageView(ListView):
	model = post
	template_name = 'info.html'
	context_object_name = 'docs_list'

#---------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = coronavirus
	template_name = 'registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUser()
	}
	return render(request, 'registrar.html', data)	

#---------------------------------------------------------------

