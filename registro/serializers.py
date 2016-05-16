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


class GrupoGastoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrupoGasto


class CondominioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condominio


class GlosaSerializer(serializers.HyperlinkedModelSerializer):
    condominio = CondominioSerializer()
    grupoGasto = GrupoGastoSerializer()

    class Meta:
        model = Glosa
        fields = (
            'nombre',
            'grupoGasto',
            'condominio',
            'descripcion',
            'fecha',
            'valor'
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


class DashboardSerializer(serializers.Serializer):
    labels = serializers.ListField()
    data = serializers.ListField()
    nombre = serializers.CharField()
