from django.db import models
from datetime import datetime  
from django.utils import timezone

# Create your models here.

MESES = (
    ('Enero','Enero'),
    ('Febrero', 'Febrero'),
    ('Marzo', 'Marzo'),
    ('Abril','Abril'),
    ('Mayo', 'Mayo'),
    ('Junio', 'Junio'),
    ('Julio','Julio'),
    ('Agosto', 'Gato'),
    ('Septiembre', 'Septiembre'),
    ('Octubre','Octubre'),
    ('Noviembre', 'Noviembre'),
    ('Diciembre', 'Diciembre')
)

class Clientes(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de cliente")
    patente = models.CharField(max_length=20,verbose_name="Patente")
    mes = models.CharField(max_length=50,choices=MESES, verbose_name='Fecha' )
    dia = models.PositiveIntegerField()
    age = models.IntegerField()
    detalles = models.CharField(max_length=150, verbose_name="Detalles ")
    total = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"Nombre: {self.nombre} Patente {self.patente}"
    