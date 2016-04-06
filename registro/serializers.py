from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import Ciudad, Comuna, AdministradorEdificio, Conserje
from rest_framework import serializers


class ConserjeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conserje


class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comuna


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad


class AdministradorEdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdministradorEdificio


class CondominioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Condominio


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Edificio


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento


class ServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Servicio


class LecturaServicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LecturaServicio
