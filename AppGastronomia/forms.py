from django import forms

class CalificacionFormulario(forms.Form):
    plato = forms.CharField()
    tipodeplato = forms.CharField()
    puntaje = forms.IntegerField()