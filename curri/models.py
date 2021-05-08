from django.db import models

class post (models.Model):
	name = models.CharField(default = "",null=True,max_length = 200)
	descripcion = models.TextField(default = "",null=True,max_length = 200)
	fecha = models.CharField(default = "",null=True,max_length = 200)
	autor = models.CharField(default = "",null=True,max_length = 200)
	
	def __str__ (self):
		return self.name