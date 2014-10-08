from django import forms
from django.forms import ModelForm
from .models import *
import pdb
tipos=(('private','Privado'),('public','Publico'),('protected','Protegido'),)
class comentarios(ModelForm):
	class Meta:
		model=comentarios
		exclude=["Usuarios"]
class preguntas(ModelForm):
	class Meta:
		model=preguntas