from django.db import models
from django.contrib import admin

# Create your models here.
class Ciudad(models.Model):
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)


class Comuna(models.Model):
    nombre=models.CharField(max_length=50)
    ciudad=models.ForeignKey(Ciudad)

    def __str__(self):
        return str(self.nombre)


class Residente(models.Model):
    rut=models.CharField(max_length=13)
    nombres=models.CharField(max_length=100)
    apellido_paterno=models.CharField(max_length=100)
    apellido_materno=models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero=models.CharField(max_length=1, choices=GENDER_CHOICES)
    fono=models.IntegerField()
    email=models.CharField(max_length=50)
    fecha_ingreso=models.DateTimeField()

    def __str__(self):
        return self.nombres


class AdministradorEdificio(models.Model):
    nombreEmpresa=models.CharField(max_length=50)
    rutEmpresa=models.CharField(max_length=13)
    razonSocial=models.CharField(max_length=50)
    fono=models.IntegerField()
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ciudad=models.ForeignKey(Ciudad)
    comuna=models.ForeignKey(Comuna)
    url=models.CharField(max_length=100)

    def __str__(self):
        return str(self.nombreEmpresa)


class Condominio(models.Model):
    nombre=models.CharField(max_length=50)
    fono=models.IntegerField()
    direccion=models.CharField(max_length=50)
    reglamento=models.CharField(max_length=100)#FileField
    ciudad=models.ForeignKey(Ciudad)
    comuna=models.ForeignKey(Comuna)
    administradorEdificio=models.ForeignKey(AdministradorEdificio)

    def __str__(self):
        return str(self.nombre)


class Edificio(models.Model):
    nombre=models.CharField(max_length=30)
    cantidadPisos=models.IntegerField()
    condominio=models.ForeignKey(Condominio)

    def __str__(self):
        return str(self.nombre)


class Departamento(models.Model):
    numero=models.IntegerField()
    metrosCuadrados=models.CharField(max_length=100)
    cantidadBanos=models.IntegerField(default=1)
    cantidadPiezas=models.IntegerField(default=1)
    walkInCloset=models.BooleanField(default=True)
    edificio=models.ForeignKey(Edificio)

    def __str__(self):
        return str(self.numero)


class Contrato(models.Model):
    departamento=models.ForeignKey(Departamento)
    residente=models.ForeignKey(Residente)
    fecha_inicio=models.DateTimeField()
    fecha_termino=models.DateTimeField()
    RESIDENT_CHOICES = (
        ('P', 'Propietario'),
        ('A', 'Arrendatario'),
    )
    tipo=models.CharField(max_length=1, choices=RESIDENT_CHOICES)

    def __str__(self):
        return str(self.departamento__numero)


class Conserje(models.Model):
    rut=models.CharField(max_length=13)
    nombres=models.CharField(max_length=100)
    apellido_paterno=models.CharField(max_length=100)
    apellido_materno=models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    genero=models.CharField(max_length=1, choices=GENDER_CHOICES)
    fono=models.IntegerField()
    email=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    comuna=models.ForeignKey(Comuna)
    ciudad=models.ForeignKey(Ciudad)
    departamento=models.ForeignKey(Departamento)
    TURN_CHOICES = (
        ('D', 'Diurno'),
        ('N', 'Nocturno'),
    )
    turno=models.CharField(max_length=1, choices=TURN_CHOICES)
    activo=models.BooleanField(default=True)

    def __str__(self):
        return self.nombres

class ResidenteAdmin(admin.ModelAdmin):
    model=Residente
    list_display=('rut', 'nombres', 'apellido_paterno',
                  'apellido_materno', 'genero', 'fono',
                  'email','fecha_ingreso')
    list_filter=('rut', 'nombres', 'apellido_paterno',
                 'apellido_materno', 'genero', 'fono',
                 'email','fecha_ingreso')
    search_fields=('rut', 'nombres', 'apellido_paterno',
                   'apellido_materno', 'genero', 'fono',
                   'email','fecha_ingreso')

class DepartamentoAdmin(admin.ModelAdmin):
    model=Departamento
    list_display=['numero', 'metrosCuadrados', 'cantidadBanos',
                  'cantidadPiezas', 'walkInCloset', 'get_nombre_edificio']
    list_filter=['numero', 'metrosCuadrados', 'cantidadBanos',
                 'cantidadPiezas', 'walkInCloset'] #hay que filtrar edificio
    search_fields=['numero', 'metrosCuadrados', 'cantidadBanos',
                  'cantidadPiezas', 'walkInCloset', 'get_nombre_edificio']

    def get_nombre_edificio(self, obj):
        return obj.edificio.nombre

    get_nombre_edificio.admin_order_field  = 'edificio'  #Allows column order sorting
    get_nombre_edificio.short_description  = 'Edificio'  #Renames column head

class CondominioAdmin(admin.ModelAdmin):
    model=Condominio
    list_display=('nombre', 'fono', 'direccion', 'ciudad',
                  'comuna', 'get_nombre_empresa')
    list_filter=('nombre', 'fono', 'direccion', 'ciudad',
                 'comuna') #hay que filtrar empresa
    search_fields=('nombre', 'fono', 'direccion', 'ciudad',
                   'comuna', 'get_nombre_empresa')

    def get_nombre_empresa(self, obj):
        return obj.administradorEdificio.nombreEmpresa

    get_nombre_empresa.admin_order_field  = 'administradorEdificio'  #Allows column order sorting
    get_nombre_empresa.short_description  = 'Empresa'  #Renames column head

class EdificioAdmin(admin.ModelAdmin):
    model=Edificio
    list_display=('nombre', 'cantidadPisos', 'get_nombre_condominio')
    list_filter=('nombre', 'cantidadPisos') #hay que filtrat condominio
    search_fields=('nombre', 'cantidadPisos', 'get_nombre_condominio')

    def get_nombre_condominio(self, obj):
        return obj.condominio.nombre

    get_nombre_condominio.admin_order_field  = 'condominio'  #Allows column order sorting
    get_nombre_condominio.short_description  = 'Condominio'  #Renames column head

class ConserjeAdmin(admin.ModelAdmin):
    model=Conserje
    list_display=('rut', 'nombres', 'apellido_paterno',
                  'apellido_materno', 'genero', 'fono',
                  'email', 'direccion', 'get_nombre_comuna',
                  'get_nombre_ciudad', 'departamento', 'turno',
                  'activo')
    list_filter=('rut', 'nombres', 'apellido_paterno',
                  'apellido_materno', 'genero', 'fono',
                  'email', 'direccion', #hay que filtrar comuna
                  'departamento', 'turno', #hay que filtrar ciudad
                  'activo')
    search_fields=('rut', 'nombres', 'apellido_paterno',
                  'apellido_materno', 'genero', 'fono',
                  'email', 'direccion', 'get_nombre_comuna',
                  'get_nombre_ciudad', 'departamento', 'turno',
                  'activo')

    def get_nombre_comuna(self, obj):
        return obj.comuna.nombre

    get_nombre_comuna.admin_order_field  = 'comuna'  #Allows column order sorting
    get_nombre_comuna.short_description  = 'Comuna'  #Renames column head

    def get_nombre_ciudad(self, obj):
        return obj.ciudad.nombre

    get_nombre_ciudad.admin_order_field  = 'ciudad'  #Allows column order sorting
    get_nombre_ciudad.short_description  = 'Ciudad'  #Renames column head

class ContratoAdmin(admin.ModelAdmin):
    model=Contrato
    list_display=('get_numero_departamento', 'get_nombre_residente',
                  'fecha_inicio', 'fecha_termino', 'tipo')
    list_filter=('fecha_inicio', 'fecha_termino', 'tipo') #hay que agregar filtro residente y departamento
    search_fields = ('get_numero_departamento', 'get_nombre_residente',
                     'fecha_inicio', 'fecha_termino', 'tipo')

    def get_numero_departamento(self, obj):
        return obj.departamento.numero

    get_numero_departamento.admin_order_field  = 'departamento'  #Allows column order sorting
    get_numero_departamento.short_description  = 'Depto'  #Renames column head

    def get_nombre_residente(self, obj):
        return obj.residente.nombre

    get_nombre_residente.admin_order_field  = 'residente'  #Allows column order sorting
    get_nombre_residente.short_description  = 'Residente'  #Renames column head


class AdministradorEdificioAdmin(admin.ModelAdmin):
    model=AdministradorEdificio
    list_display=('nombreEmpresa','rutEmpresa', 'razonSocial',
                  'fono', 'email', 'direccion', 'get_nombre_comuna',
                  'get_nombre_ciudad', 'url')
    list_filter=('nombreEmpresa','rutEmpresa', 'razonSocial',
                  'fono', 'email', 'direccion', #hay que agregar filtro comuna
                  'url') #hay que filtrar ciudad
    search_fields=('nombreEmpresa','rutEmpresa', 'razonSocial',
                  'fono', 'email', 'direccion', 'get_nombre_comuna',
                  'get_nombre_ciudad', 'url')

    def get_nombre_comuna(self, obj):
        return obj.comuna.nombre

    get_nombre_comuna.admin_order_field  = 'comuna'  #Allows column order sorting
    get_nombre_comuna.short_description  = 'Comuna'  #Renames column head

    def get_nombre_ciudad(self, obj):
        return obj.ciudad.nombre

    get_nombre_ciudad.admin_order_field  = 'ciudad'  #Allows column order sorting
    get_nombre_ciudad.short_description  = 'Ciudad'  #Renames column head

class CiudadAdmin(admin.ModelAdmin):
    model=Ciudad
    list_display=('nombre',)
    list_filter=('nombre',) #hay que filtrar ciudad
    search_fields=('nombre',)

class ComunaAdmin(admin.ModelAdmin):
    model=Comuna
    list_display=('nombre', 'get_nombre_ciudad')
    list_filter=('nombre',) #hay que filtrar ciudad
    search_fields=('nombre', 'get_nombre_ciudad')

    def get_nombre_ciudad(self, obj):
        return obj.ciudad.nombre


admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Conserje, ConserjeAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(AdministradorEdificio, AdministradorEdificioAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Comuna, ComunaAdmin)
