from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from rest_framework import serializers


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
