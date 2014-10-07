from django import forms
from django.forms import ModelForm
from .models import *
import pdb

#class Usuarios(ModelForm):
#	class meta:
class comentarios(ModelForm):
	class Meta:
		model=comentarios
		exclude=["Usuarios"]
class categorias(ModelForm):
	class Meta:
		model=categorias