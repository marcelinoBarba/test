from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	titulo = models.CharField(max_length=120)
	imagen = models.FileField(null=True, blank=True)
	contenido = models.TextField()
	actualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
	creado = models.DateTimeField(auto_now=False, auto_now_add=True)


	def _unicode_(self):
		return self.titulo