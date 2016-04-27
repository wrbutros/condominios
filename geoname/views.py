from rest_framework import viewsets

from models import Comuna, Ciudad
from serializers import CiudadSerializer, ComunaSerializer


class ComunaSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class CiudadSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
