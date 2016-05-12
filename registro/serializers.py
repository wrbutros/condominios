from rest_framework import serializers

from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import AdministradorEdificio, Conserje, MultaEInteres, PagoYAbono


class ConserjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conserje


class AdministradorEdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdministradorEdificio


class CondominioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condominio


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


class DashboardSerializer(serializers.Serializer):
    labels = serializers.ListField()
    data = serializers.ListField()
    nombre = serializers.CharField()
