from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.views import View
from AppGastronomia.models import Postre, Comida, Bebida, Calificacion
from AppGastronomia.forms import CalificacionFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):

    return render(request, "AppGastronomia/inicio.html")

def comidas(request):
    comidas = Comida.objects.all()
    return render(request, 'AppGastronomia/comida.html', {'Comidas':comidas})

def create_comida(request):
    if request.method == 'POST':
        comida = Comida()
        comida.name= request.POST['name']
        comida.tipo_de_plato= request.POST['tipo de plato']
        comida.save()
    return redirect('inicio/')


def bebidas(request):
    Bebidas = Bebida.objects.all()
    return render(request, 'AppGastronomia/bebidas.html', {'Bebidas':Bebidas})

def postres(request):
    Postres = Postre.objects.all()
    return render(request, 'AppGastronomia/postre.html', { 'Postres':Postres})

def new_func():
    comida = comida()
    return comida

from AppGastronomia.forms import CalificacionFormulario

def calificacion(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
      
        miFormulario = CalificacionFormulario(request.POST) 
        print(miFormulario)
        
        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            plato = plato(
                nombre=informacion["plato"], tipodeplato = informacion["Tipo de plato"], puntaje=informacion["puntaje"])

            plato.save()


            return render(request, "ApGastronomia/inicio.html")

        else:

            miFormulario = CalificacionFormulario()
    return render(request, "AppGastroomia/calificacion.html", {"miFormulario": miFormulario})

def busquedaCalificacion(request):
    return render(request, "AppGastroomia/busquedacalificacion.html")

def buscar(request):
    
    respuesta = f"Estoy buscando el plato: {request.GET['plato']}"
    
    #No olvidar from django.http import HttpResponsereturn HttpResponse(respuesta)
    return HttpResponse(respuesta)