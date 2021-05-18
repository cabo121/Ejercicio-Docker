from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)

class curriculum (models.Model):
	nombre = models.CharField(default = "",null=True,max_length = 200)
	telefono = models.CharField(default = "",null=True,max_length = 200)
	correo = models.CharField(default = "",null=True,max_length = 200)
	edad = models.CharField(default = "",null=True,max_length = 200)
	educacion = models.TextField(default = "",null=True,max_length = 200)
	experiencia = models.TextField(default = "",null=True,max_length = 200)
	aptitudes = models.TextField(default = "",null=True,max_length = 200)

	def __str__ (self):
		return self.nombre

class info (models.Model):
	instituto = models.TextField(default = "",null=True,max_length = 200)
	nombre = models.TextField(default = "",null=True,max_length = 200)
	historia = models.CharField(default = "",null=True,max_length = 200)
	eventos = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.instituto

