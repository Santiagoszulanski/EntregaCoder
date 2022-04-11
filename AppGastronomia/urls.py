from django import views
from django.urls import path
from.views import bebidas, comidas, postres

from AppGastronomia import views

urlpatterns = [
        path('', views.inicio, name="Inicio"),
        path('comidas', views.comidas, name='Comidas'),
        path('bebidas', views.bebidas, name='Bebidas'),
        path('postres', views.postres, name='Postres'),
        path('calificacion', views.calificacion, name="Calificacion"),
        path('busquedaplato', views.busquedaCalificacion, name="BusquedaPlato"),
        path('buscar/', views.buscar),
]
