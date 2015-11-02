from django.db import models
from django.contrib import admin

# Create your models here.
class Propietario(models.Model):
    rut=models.CharField(max_length=13)
    nombres=models.CharField(max_length=100)
    apellido_paterno=models.CharField(max_length=100)
    apellido_materno=models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero=models.CharField(max_length=1, choices=GENDER_CHOICES)
    fecha_ingreso=models.DateTimeField()

    def __str__(self):
        return self.nombres

class Departamento(models.Model):
    numero=models.IntegerField()
    propietario=models.ForeignKey(Propietario)

    def __str__(self):
        return str(self.numero)

class PropietarioAdmin(admin.ModelAdmin):
    list_display=('rut', 'nombres', 'apellido_paterno',
                  'apellido_materno', 'genero', 'fecha_ingreso')
    list_filter=('rut', 'nombres', 'apellido_paterno',
                 'apellido_materno', 'genero', 'fecha_ingreso')
    search_fields=('rut', 'nombres', 'apellido_paterno',
                   'apellido_materno', 'genero', 'fecha_ingreso')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('numero', 'propietario')
    list_filter=('numero', 'propietario')
    search_fields = ['numero', 'propietario__nombres']

admin.site.register(Propietario, PropietarioAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
