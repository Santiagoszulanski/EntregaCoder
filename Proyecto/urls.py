from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/AppGastronomia/', permanent=True)), # Para que ingrese directamente a nuestra pagina
    path('AppGastronomia/', include('AppGastronomia.urls')),
]


