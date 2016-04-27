from rest_framework import serializers
from models import Ciudad, Comuna


class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comuna


class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
