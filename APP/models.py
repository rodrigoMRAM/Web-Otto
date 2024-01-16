from django.db import models
from datetime import datetime  
from django.utils import timezone

# Create your models here.



class Clientes(models.Model):
    MESES = [
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
    ]

    AGES = [
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
    (2026, 2026),
    (2027, 2027),
    (2028, 2028),
    (2029, 2029),
    (2030, 2030),
    (2031, 2031)
]
    nombre = models.CharField(max_length=50, verbose_name="Nombre de cliente")
    patente = models.CharField(max_length=20,verbose_name="Patente")
    mes = models.CharField(max_length=50,choices=MESES, verbose_name='Fecha' )
    dia = models.PositiveIntegerField()
    age = models.IntegerField(choices=AGES, verbose_name="Año")
    detalles = models.CharField(max_length=150, verbose_name="Detalles ")
    total = models.FloatField(null=True, blank=True)


    def __str__(self):
        return f"Nombre: {self.nombre} Patente {self.patente}"
    