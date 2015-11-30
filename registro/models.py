from django.db import models
from django.core.validators import MaxLengthValidator


class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad)

    def __str__(self):
        return str(self.nombre)


class GrupoGasto(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "GruposGasto"

    def __unicode__(self):
        return self.nombre

class TipoGasto(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    grupoGasto = models.ForeignKey(GrupoGasto)

    class Meta:
        verbose_name_plural = "TiposGasto"

    def __unicode__(self):
        return self.nombre


class Residente(models.Model):
    rut = models.CharField(max_length=13)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fono = models.IntegerField()
    email = models.CharField(max_length=50)
    fecha_ingreso = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres


class AdministradorEdificio(models.Model):
    nombreEmpresa = models.CharField(max_length=50)
    rutEmpresa = models.CharField(max_length=13)
    razonSocial = models.CharField(max_length=50)
    fono = models.IntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad)
    comuna = models.ForeignKey(Comuna)
    url = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombreEmpresa)


class Conserje(models.Model):
    rut = models.CharField(max_length=13)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    fono = models.IntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    comuna = models.ForeignKey(Comuna)
    ciudad = models.ForeignKey(Ciudad)
    #    TURN_CHOICES = (
    #        ('D', 'Diurno'),
    #        ('N', 'Nocturno'),
    #    )
    #    turno=models.CharField(max_length=1, choices=TURN_CHOICES)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombres


class Condominio(models.Model):
    nombre = models.CharField(max_length=50)
    fono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    reglamento = models.CharField(max_length=100)  # FileField
    ciudad = models.ForeignKey(Ciudad)
    comuna = models.ForeignKey(Comuna)
    administradorEdificio = models.ForeignKey(AdministradorEdificio)
    conserjes = models.ManyToManyField(Conserje, related_name='condominios')

    def __str__(self):
        return str(self.nombre)


class GastoCondominio(models.Model):
    grupoGasto = models.ForeignKey(GrupoGasto)
    tipoGasto = models.ForeignKey(TipoGasto)
    condominio = models.ForeignKey(Condominio)
    egreso = models.CharField(max_length=50)
    descripcion =  models.TextField(validators=[MaxLengthValidator(500)])
    fecha = models.DateTimeField()
    valor = models.IntegerField()

    def __str__(self):
        return str(self.valor)


class Edificio(models.Model):
    nombre = models.CharField(max_length=30)
    cantidadPisos = models.IntegerField()
    condominio = models.ForeignKey(Condominio)

    def __str__(self):
        return str(self.nombre)


class Departamento(models.Model):
    numero = models.IntegerField()
    metrosCuadrados = models.CharField(max_length=100)
    cantidadBanos = models.IntegerField(default=1)
    cantidadPiezas = models.IntegerField(default=1)
    walkInCloset = models.BooleanField(default=True)
    edificio = models.ForeignKey(Edificio)

    def __str__(self):
        return str(self.numero)


class Contrato(models.Model):
    departamento = models.ForeignKey(Departamento)
    residente = models.ForeignKey(Residente)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField(blank=True)
    RESIDENT_CHOICES = (
        ('P', 'Propietario'),
        ('A', 'Arrendatario'),
    )
    tipo = models.CharField(max_length=1, choices=RESIDENT_CHOICES)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.tipo)
