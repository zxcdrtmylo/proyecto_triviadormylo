from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection

class preguntas(models.Model):
	nombre=models.CharField(max_length=300)
	def __unicode__(self):
		return "->%s "%(self.nombre)
class comentarios(models.Model):
	contenido=models.TextField()
	fecha=models.DateField(auto_now=ture)
	email=models.EmailField()
	usuario=models.ForeignKey(User)