from django.db import models
from datetime import datetime  

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de cliente: ")
    patente = models.CharField(max_length=20,verbose_name="Patente: ")
    fechaDeIngreso = models.DateTimeField(default=datetime.now, verbose_name='Fecha')
    detalles = models.CharField(max_length=150, verbose_name="Detalles: ")
    total = models.FloatField(null=True, blank=True)
    def __str__(self):
        return f"Nombre: {self.nombre} Patente {self.patente}"
    