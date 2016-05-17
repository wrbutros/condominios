from rest_framework import serializers

from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import AdministradorEdificio, Conserje, MultaEInteres, PagoYAbono
from models import Contrato, Residente, GrupoGasto, Glosa


class ConserjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conserje


class AdministradorEdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdministradorEdificio


class CondominioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condominio


class GrupoGastoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrupoGasto
        fields = (
            'nombre',
            'activo'
        )


class GlosaSerializer(serializers.HyperlinkedModelSerializer):
    condominio = CondominioSerializer()
    grupoGasto = GrupoGastoSerializer()

    class Meta:
        model = Glosa
        fields = (
            'nombre',
            'grupoGasto',
            'descripcion',
            'nombreDocumento',
            'nombreDocumentoOrig',
            'ingreso',
            'egreso'
        )


class ResidenteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residente
        fields = (
            'rut',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'genero',
            'fono',
            'email',
            'fecha_ingreso',
            'activo'
        )


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    condominio = CondominioSerializer()

    class Meta:
        model = Edificio
        fields = (
            'nombre',
            'cantidadPisos',
            'condominio'
        )


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    edificio = EdificioSerializer()

    class Meta:
        model = Departamento
        fields = (
            'numero',
            'metrosCuadrados',
            'cantidadBanos',
            'cantidadPiezas',
            'walkInCloset',
            'porcentajeDominio',
            'edificio'
        )


class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio
        fields = (
            'nombre',
            'unidad_medida'
        )


class LecturaServicioSerializer(serializers.HyperlinkedModelSerializer):
    servicio = ServicioSerializer()
    departamento = DepartamentoSerializer()

    class Meta:
        model = LecturaServicio
        fields = (
            'servicio',
            'departamento',
            'fecha',
            'lectura'
        )


class MultaEInteresSerializer(serializers.HyperlinkedModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = MultaEInteres
        fields = (
            'departamento',
            'monto',
            'fecha'
        )


class PagoYAbonoSerializer(serializers.HyperlinkedModelSerializer):
    departamento = DepartamentoSerializer()

    class Meta:
        model = PagoYAbono
        fields = (
            'departamento',
            'monto',
            'fecha'
        )


class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    departamento = DepartamentoSerializer()
    residente  = ResidenteSerializer()

    class Meta:
        model = Contrato
        fields = (
            'departamento',
            'residente',
            'fecha_inicio',
            'fecha_termino',
            'tipo',
            'activo'
        )


class RendicionSerializer(serializers.Serializer):
    caption = serializers.CharField()
    height = serializers.IntegerField()
    hiddengrid = serializers.BooleanField()
    hidegrid = serializers.BooleanField()
    grouping = serializers.BooleanField()
    colNames = serializers.ListField()
    colModel = serializers.ListField() #No es una lista
    data = serializers.ListField() #No es una lista


class DashboardSerializer(serializers.Serializer):
    labels = serializers.ListField()
    data = serializers.ListField()
    nombre = serializers.CharField()
