from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from .models import curriculum, info
from django.contrib.auth.models import User
from .forms import curriForm,infoForm, CustomUserForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

#---------------------------------------------------------------

class HomePageView(ListView):
	model = info
	template_name = 'home.html'
	context_object_name = 'docs_list'

class CurriPageView(ListView):
	model = curriculum
	template_name = 'curriculum.html'
	context_object_name = 'docs_list'

class InfoPageView(ListView):
	model = info
	template_name = 'info.html'
	context_object_name = 'docs_list'

#---------------------------------------------------------------

class RegistrarPageView (CreateView):
	model = User
	template_name = 'registration/registrar.html'
	form_class =  UserCreationForm
	success_url = reverse_lazy('registro_success')

class RegistroPageView(ListView):
	model = info
	template_name = 'registration/registro_success.html'

class ResetPageView (CreateView):
	model = User
	form_class =  UserCreationForm
	template_name = 'registration/reset.html'
	success_url = reverse_lazy('home')

def registro_usuario (request):
	data = {
		'form': CustomUserForm()
	}

	if request.method == 'POST':
		formulario = CustomUserForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='registro_success')
		else:
			data['form'] = formulario
			
	return render(request, 'registration/registrar.html', data)	

#---------------------------------------------------------------

def agregar (request):
	data = {
		'form':curriForm()
	}

	if request.method == 'POST':
		formulario = curriForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='curriculum')
		else:
			data['form'] = formulario

	return render(request, 'agregarCurri.html',data)


def modificar (request, id):

	curri = get_object_or_404(curriculum, id=id)

	data = {
		'form': curriForm(instance=curri)
	}

	if request.method == 'POST':
		formulario = curriForm(data=request.POST, instance=curri)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='curriculum')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

def eliminar (request, id):
	curri = get_object_or_404(curriculum, id=id)
	curri.delete()

	return redirect(to = "curriculum")





def agregarInfo (request):
	data = {
		'form':infoForm()
	}

	if request.method == 'POST':
		formulario = infoForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = 'Guardado correctamente'
			return redirect(to='info')
		else:
			data['form'] = formulario

	return render(request, 'agregarInfo.html',data)


def modificarInfo (request, id):

	infod = get_object_or_404(info, id=id)

	data = {
		'form': infoForm(instance=infod)
	}

	if request.method == 'POST':
		formulario = infoForm(data=request.POST, instance=infod)
		if formulario.is_valid():
			formulario.save()
			return redirect(to='info')
		data['form'] = formulario

	return render (request, 'modificar.html', data)

def eliminarInfo (request, id):
	infod = get_object_or_404(info, id=id)
	infod.delete()

	return redirect(to = "info")


#---------------------------------------------------------------

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })

#---------------------------------------------------------------

