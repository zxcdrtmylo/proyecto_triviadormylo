from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
import datetime
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
import pdb

def preguntas(request):
	if(request.method=="POST"):
		form=preguntas(request.POST)
		if(form.is_valid()):
			form.save()
	form=preguntas()
	return render_to_response("/Inicio/preguntas.html")
def registro_usuarios(request):
	if request.method=="POST":
		form=UserCreationForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect("/Inicio/")
	form=UserCreationForm()
	return render_to_response("usuario/registro.html",{"form":form},RequestContext(request))
def login_usuario(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if(form.is_valid()==False):
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("/Inicio/perfil/")
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))
def perfil(request):
	return render_to_response("usuario/perfil.html",{'nombre':request.session["name"]},RequestContext(request))
def logout_usuario(request):
	logout(request)
	return HttpResponseRedirect("/Inicio/")
def pagina_principal(request):
	if request.method=="POST":
		form=comentarios(request.POST)
		if(form.is_valid()):
			form.save()
	fecha=datetime.datetime.now()
	return render_to_response("Inicio/principal.html",{"fecha":fecha},RequestContext(request))
def pagina_comentarios(request):
	if request.method=="POST":
		form=comentarios(request.POST)
		if(form.is_valid()):
			form.save()
	return render_to_response("Inicio/comentarios.html",{"comentarios":comentarios()},RequestContext(request))

	