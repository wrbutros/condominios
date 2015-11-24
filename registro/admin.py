from django.contrib import admin
from .models import Residente, Departamento, Condominio, Conserje
from .models import Contrato, Ciudad, Comuna, Edificio, AdministradorEdificio


##  ====== RESIDENTE =======
class ResidenteAdmin(admin.ModelAdmin):
    model = Residente
    list_display = ('rut', 'nombres', 'apellido_paterno',
                    'apellido_materno', 'genero', 'fono',
                    'email', 'fecha_ingreso')
    list_filter = ('rut', 'nombres', 'apellido_paterno',
                   'apellido_materno', 'genero', 'fono',
                   'email', 'fecha_ingreso')
    search_fields = ('rut', 'nombres', 'apellido_paterno',
                     'apellido_materno', 'genero', 'fono',
                     'email', 'fecha_ingreso')


##  ====== DEPARTAMENTO =======
class DepartamentoAdmin(admin.ModelAdmin):
    model = Departamento
    list_display = ['numero', 'metrosCuadrados', 'cantidadBanos',
                    'cantidadPiezas', 'walkInCloset', 'get_nombre_edificio']
    list_filter = ['numero', 'metrosCuadrados', 'cantidadBanos',
                   'cantidadPiezas', 'walkInCloset']  # hay que filtrar edificio
    search_fields = ['numero', 'metrosCuadrados', 'cantidadBanos',
                     'cantidadPiezas', 'walkInCloset', 'get_nombre_edificio']

    def get_nombre_edificio(self, obj):
        return obj.edificio.nombre

    get_nombre_edificio.admin_order_field = 'edificio'  # Allows column order sorting
    get_nombre_edificio.short_description = 'Edificio'  # Renames column head


##  ====== CONSERJE-CONDOMINIO =======
class ConserjeCondominioInline(admin.TabularInline):
    model = Condominio.conserjes.through


##  ====== CONSERJE =======
class ConserjeAdmin(admin.ModelAdmin):
    model = Conserje
    inlines = [
        ConserjeCondominioInline,
    ]
    list_display = ('rut', 'nombres', 'apellido_paterno',
                    'apellido_materno', 'genero', 'fono',
                    'email', 'direccion', 'get_nombre_comuna',
                    'get_nombre_ciudad', 'activo')
    list_filter = ('rut', 'nombres', 'apellido_paterno',
                   'apellido_materno', 'genero', 'fono',
                   'email', 'direccion',  # hay que filtrar comuna, ciudad
                   'activo')
    search_fields = ('rut', 'nombres', 'apellido_paterno',
                     'apellido_materno', 'genero', 'fono',
                     'email', 'direccion', 'get_nombre_comuna',
                     'get_nombre_ciudad', 'activo')

    def get_nombre_comuna(self, obj):
        return obj.comuna.nombre

    get_nombre_comuna.admin_order_field = 'comuna'  # Allows column order sorting
    get_nombre_comuna.short_description = 'Comuna'  # Renames column head

    def get_nombre_ciudad(self, obj):
        return obj.ciudad.nombre

    get_nombre_ciudad.admin_order_field = 'ciudad'  # Allows column order sorting
    get_nombre_ciudad.short_description = 'Ciudad'  # Renames column head


##  ====== CONDOMINIO =======
class CondominioAdmin(admin.ModelAdmin):
    model = Condominio
    inlines = [
        ConserjeCondominioInline,
    ]
    exlude = ('condominios',)
    list_display = ('nombre', 'fono', 'direccion', 'ciudad',
                    'comuna', 'get_nombre_empresa')
    list_filter = ('nombre', 'fono', 'direccion', 'ciudad',
                   'comuna')  # hay que filtrar empresa
    search_fields = ('nombre', 'fono', 'direccion', 'ciudad',
                     'comuna', 'get_nombre_empresa')

    def get_nombre_empresa(self, obj):
        return obj.administradorEdificio.nombreEmpresa

    get_nombre_empresa.admin_order_field = 'administradorEdificio'  # Allows column order sorting
    get_nombre_empresa.short_description = 'Empresa'  # Renames column head


##  ====== EDIFICIO =======
class EdificioAdmin(admin.ModelAdmin):
    model = Edificio
    list_display = ('nombre', 'cantidadPisos', 'get_nombre_condominio')
    list_filter = ('nombre', 'cantidadPisos')  # hay que filtrat condominio
    search_fields = ('nombre', 'cantidadPisos', 'get_nombre_condominio')

    def get_nombre_condominio(self, obj):
        return obj.condominio.nombre

    get_nombre_condominio.admin_order_field = 'condominio'  # Allows column order sorting
    get_nombre_condominio.short_description = 'Condominio'  # Renames column head


##  ====== CONTRATO =======
class ContratoAdmin(admin.ModelAdmin):
    model = Contrato
    list_display = ('get_numero_departamento', 'get_nombre_residente',
                    'fecha_inicio', 'fecha_termino', 'tipo')
    list_filter = ('fecha_inicio', 'fecha_termino',
                   'tipo')  # hay que agregar filtro residente y departamento
    search_fields = ('get_numero_departamento', 'get_nombre_residente',
                     'fecha_inicio', 'fecha_termino', 'tipo')

    def get_numero_departamento(self, obj):
        return obj.departamento.numero

    get_numero_departamento.admin_order_field = 'departamento'  # Allows column order sorting
    get_numero_departamento.short_description = 'Depto'  # Renames column head

    def get_nombre_residente(self, obj):
        return obj.residente.nombres

    get_nombre_residente.admin_order_field = 'residente'  # Allows column order sorting
    get_nombre_residente.short_description = 'Residente'  # Renames column head


##  ====== ADMINISTRADOR EDIFICIO =======
class AdministradorEdificioAdmin(admin.ModelAdmin):
    model = AdministradorEdificio
    list_display = ('nombreEmpresa', 'rutEmpresa', 'razonSocial',
                    'fono', 'email', 'direccion', 'get_nombre_comuna',
                    'get_nombre_ciudad', 'url')
    list_filter = ('nombreEmpresa', 'rutEmpresa', 'razonSocial',
                   'fono', 'email', 'direccion',
                   # hay que agregar filtro comuna
                   'url')  # hay que filtrar ciudad
    search_fields = ('nombreEmpresa', 'rutEmpresa', 'razonSocial',
                     'fono', 'email', 'direccion', 'get_nombre_comuna',
                     'get_nombre_ciudad', 'url')

    def get_nombre_comuna(self, obj):
        return obj.comuna.nombre

    get_nombre_comuna.admin_order_field = 'comuna'  # Allows column order sorting
    get_nombre_comuna.short_description = 'Comuna'  # Renames column head

    def get_nombre_ciudad(self, obj):
        return obj.ciudad.nombre

    get_nombre_ciudad.admin_order_field = 'ciudad'  # Allows column order sorting
    get_nombre_ciudad.short_description = 'Ciudad'  # Renames column head


##  ====== CIUDAD =======
class CiudadAdmin(admin.ModelAdmin):
    model = Ciudad
    list_display = ('nombre',)
    list_filter = ('nombre',)  # hay que filtrar ciudad
    search_fields = ('nombre',)


##  ====== COMUNA =======
class ComunaAdmin(admin.ModelAdmin):
    model = Comuna
    list_display = ('nombre', 'get_nombre_ciudad')
    list_filter = ('nombre',)  # hay que filtrar ciudad
    search_fields = ('nombre', 'get_nombre_ciudad')

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
