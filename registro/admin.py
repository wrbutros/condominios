from django.contrib import admin
from .models import Residente, Departamento, Condominio, Conserje
from .models import Contrato, Edificio, AdministradorEdificio
from .models import GrupoGasto, TipoGasto, GastoCondominio
from .models import Estacionamiento, Comite, CargoComite, Bodega
from .models import Servicio, LecturaServicio, Cobranza
from .models import TipoMultaEInteres, MultaCondominio, MultaEInteres
from .models import PagoYAbono, BalanceMensual

from geoname.models import Ciudad, Comuna

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
                    'cantidadPiezas', 'walkInCloset', 'porcentajeDominio',
                    'get_nombre_edificio']
    list_filter = ['numero', 'metrosCuadrados', 'cantidadBanos',
                   'cantidadPiezas', 'walkInCloset']  # hay que filtrar edificio
    search_fields = ['numero', 'metrosCuadrados', 'cantidadBanos',
                     'cantidadPiezas', 'walkInCloset', 'get_nombre_edificio']

    def get_nombre_edificio(self, obj):
        return obj.edificio.nombre

    get_nombre_edificio.admin_order_field = 'edificio'  # Allows column order sorting
    get_nombre_edificio.short_description = 'Edificio'  # Renames column head


##  ====== ESTACIONAMIENTO =======
class EstacionamientoAdmin(admin.ModelAdmin):
    model = Estacionamiento
    list_display = ['numero', 'porcentajeDominio', 'get_numero_departamento']
    list_filter = ['numero']  # hay que filtrar departamento
    search_fields = ['numero', 'get_numero_departamento']

    def get_numero_departamento(self, obj):
        return obj.departamento.numero

    get_numero_departamento.admin_order_field = 'estacionamiento'  # Allows column order sorting
    get_numero_departamento.short_description = 'Estacionamiento'  # Renames column head


##  ====== BODEGA =======
class BodegaAdmin(admin.ModelAdmin):
    model = Bodega
    list_display = ['numero', 'porcentajeDominio', 'get_numero_departamento']
    list_filter = ['numero']  # hay que filtrar departamento
    search_fields = ['numero', 'get_numero_departamento']

    def get_numero_departamento(self, obj):
        return obj.departamento.numero

    get_numero_departamento.admin_order_field = 'bodega'  # Allows column order sorting
    get_numero_departamento.short_description = 'Bodega'  # Renames column head


##  ====== CARGO COMITE =======
class CargoComiteAdmin(admin.ModelAdmin):
    model = CargoComite
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']


##  ====== COMITE =======
class ComiteAdmin(admin.ModelAdmin):
    model = Comite
    list_display = ('get_cargo_comite', 'nombre', 'fecha_inicio', 'fecha_termino',
                    'activo', 'get_nombre_condominio')
    list_filter = ('nombre', 'fecha_inicio', 'fecha_termino', 'activo')  # agregar filtro comite y condominio
    search_fields = ('get_cargo_comite', 'nombre', 'fecha_inicio', 'fecha_termino',
                     'activo', 'get_nombre_condominio')

    def get_cargo_comite(self, obj):
        return obj.cargo.nombre

    def get_nombre_condominio(self, obj):
        return obj.condominio.nombre


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


##  ====== GRUPO GASTO =======
class GrupoGastoAdmin(admin.ModelAdmin):
    model = GrupoGasto
    list_display = ('nombre', 'activo')
    list_filter = ('nombre', 'activo')
    search_fields = ('nombre', 'activo')


##  ====== GASTO =======
class TipoGastoAdmin(admin.ModelAdmin):
    model = TipoGasto
    list_display = ('nombre', 'activo', 'get_grupo_gasto')
    list_filter = ('nombre', 'activo')
    search_fields = ('nombre', 'activo', 'get_grupo_gasto')

    def get_grupo_gasto(self, obj):
        return obj.grupoGasto.nombre


##  ====== GASTO CONDOMINIO =======
class GastoCondominioAdmin(admin.ModelAdmin):
    model = GastoCondominio
    list_display = ('get_tipo_gasto', 'get_condominio',
                    'egreso', 'fecha', 'valor')
    list_filter = ('egreso', 'fecha', 'valor')
    search_fields = ('get_tipo_gasto', 'get_condominio',
                     'egreso', 'fecha', 'valor')

    def get_grupo_gasto(self, obj):
        return obj.grupoGasto.nombre

    def get_tipo_gasto(self, obj):
        return obj.tipoGasto.nombre

    def get_condominio(self, obj):
        return obj.condominio.nombre


##  ====== SERVICIO =======
class ServicioAdmin(admin.ModelAdmin):
    model = Servicio
    list_display = ('nombre', 'unidad_medida')
    list_filter = ('nombre', 'unidad_medida')
    search_fields = ('nombre', 'unidad_medida')


##  ====== LECTURA SERVICIO =======
class LecturaServicioAdmin(admin.ModelAdmin):
    model = LecturaServicio
    list_display = ('get_servicio', 'get_departamento', 'fecha', 'lectura')
    list_filter = ('fecha', 'lectura')
    search_fields = ('get_servicio', 'get_departamento', 'fecha', 'lectura')

    def get_servicio(self, obj):
        return obj.servicio.nombre

    def get_departamento(self, obj):
        return obj.departamento.numero


##  ====== Tipo Multa E Interes =======
class TipoMultaEInteresAdmin(admin.ModelAdmin):
    model = TipoMultaEInteres
    list_display = ('nombre',)
    list_filter = ('nombre',)
    search_fields = ('nombre',)


##  ====== Multa Condominio =======
class MultaCondominioAdmin(admin.ModelAdmin):
    model = MultaCondominio
    list_display = ('get_tipoMultaEInteres', 'get_condominio', 'porcentajeMulta')
    list_filter = ('porcentajeMulta',)
    search_fields = ('get_tipoMultaEInteres', 'get_condominio', 'porcentajeMulta')

    def get_tipoMultaEInteres(self, obj):
        return obj.TipoMultaEInteres.nombre

    def get_condominio(self, obj):
        return obj.condominio.nombre


##  ====== Multa E Interes =======
class MultaEInteresAdmin(admin.ModelAdmin):
    model = MultaEInteres
    list_display = ('get_departamento', 'monto', 'fecha')
    list_filter = ('monto', 'fecha')
    search_fields = ('get_departamento', 'monto', 'fecha')

    def get_departamento(self, obj):
        return obj.departamento.numero


##  ====== Pago Y Abono =======
class PagoYAbonoAdmin(admin.ModelAdmin):
    model = PagoYAbono
    list_display = ('get_departamento', 'monto', 'fecha')
    list_filter = ('monto', 'fecha')
    search_fields = ('get_departamento', 'monto', 'fecha')

    def get_departamento(self, obj):
        return obj.departamento.numero


##  ====== Balance Mensual =======
class BalanceMensualAdmin(admin.ModelAdmin):
    model = BalanceMensual
    list_display = ('get_departamento', 'monto', 'fecha')
    list_filter = ('monto', 'fecha')
    search_fields = ('get_departamento', 'monto', 'fecha')

    def get_departamento(self, obj):
        return obj.departamento.numero


## ======= MODELO COBRANZA (SOLO PARA EFECTOS VISUALES) =======
class CobranzaAdmin(admin.ModelAdmin):
    model = Cobranza
    list_display = ('get_edificio', 'get_departamento', 'porcentajeDominio',
                    'gastosComunes', 'fondoDeReserva', 'lecturaAnterior',
                    'lecturaActual', 'aguaCalienteM3', 'aguaCalienteCosto',
                    'multasEIntereses', 'morosidad', 'diferenciaAFavor',
                    'cobroTransbank', 'totalACobrar', 'observaciones')

    list_filter = ('porcentajeDominio',
                   'gastosComunes', 'fondoDeReserva', 'lecturaAnterior',
                   'lecturaActual', 'aguaCalienteM3', 'aguaCalienteCosto',
                   'multasEIntereses', 'morosidad', 'diferenciaAFavor',
                   'cobroTransbank', 'totalACobrar', 'observaciones')

    search_fields = ('get_edificio', 'get_departamento', 'porcentajeDominio',
                     'gastosComunes', 'fondoDeReserva', 'lecturaAnterior',
                     'lecturaActual', 'aguaCalienteM3', 'aguaCalienteCosto',
                     'multasEIntereses', 'morosidad', 'diferenciaAFavor',
                     'cobroTransbank', 'totalACobrar', 'observaciones')

    def get_departamento(self, obj):
        return obj.departamento.numero

    def get_edificio(self, obj):
        return obj.edificio.nombre


admin.site.register(Residente, ResidenteAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Condominio, CondominioAdmin)
admin.site.register(Edificio, EdificioAdmin)
admin.site.register(Estacionamiento, EstacionamientoAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Comite, ComiteAdmin)
admin.site.register(CargoComite, CargoComiteAdmin)
admin.site.register(Conserje, ConserjeAdmin)
admin.site.register(Contrato, ContratoAdmin)
admin.site.register(AdministradorEdificio, AdministradorEdificioAdmin)

admin.site.register(GrupoGasto, GrupoGastoAdmin)
admin.site.register(TipoGasto, TipoGastoAdmin)
admin.site.register(GastoCondominio, GastoCondominioAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(LecturaServicio, LecturaServicioAdmin)
admin.site.register(Cobranza, CobranzaAdmin)

admin.site.register(TipoMultaEInteres, TipoMultaEInteresAdmin)
admin.site.register(MultaCondominio, MultaCondominioAdmin)
admin.site.register(MultaEInteres, MultaEInteresAdmin)
admin.site.register(PagoYAbono, PagoYAbonoAdmin)
admin.site.register(BalanceMensual, BalanceMensualAdmin)
