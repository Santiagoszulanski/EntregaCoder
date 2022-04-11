from django.db import models

class Postre(models.Model):
    nombre=models.CharField(max_length=40)
    tipodepostre = models.CharField(max_length=30)


class Comida(models.Model):
    nombre= models.CharField(max_length=30)
    tipodeplato= models.CharField(max_length=30)

    def __str__(self):
        return f"Plato: {self.plato} - Tipodeplato: {self.tipodeplato}"

class Bebida(models.Model):
    nombre= models.CharField(max_length=30)
    tipodebebida= models.CharField(max_length=30)

    def __str__(self):
        return f"Bebida: {self.bebida} - Tipodeplato: {self.tipodebebida}"

class Calificacion(models.Model):
    nombre= models.CharField(max_length=30)
    puntaje= models.IntegerField()
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()
