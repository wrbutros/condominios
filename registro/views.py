from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics

from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import Comuna, Ciudad, AdministradorEdificio, Conserje

from serializers import CondominioSerializer, EdificioSerializer
from serializers import DepartamentoSerializer, ServicioSerializer
from serializers import LecturaServicioSerializer, CiudadSerializer
from serializers import ComunaSerializer, AdministradorEdificioSerializer
from serializers import ConserjeSerializer


def dashboard(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/dashboard.html', context)


def index(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/index.html', context)


class ConserjeSet(viewsets.ModelViewSet):
    queryset = Conserje.objects.all()
    serializer_class = ConserjeSerializer


class ComunaSet(viewsets.ModelViewSet):
    queryset = Comuna.objects.all()
    serializer_class = ComunaSerializer


class CiudadSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer


class AdministradorEdificioSet(viewsets.ModelViewSet):
    queryset = AdministradorEdificio.objects.all()
    serializer_class = AdministradorEdificioSerializer


class CondominioSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer


class EdificioSet(viewsets.ModelViewSet):
    queryset = Edificio.objects.all()
    serializer_class = EdificioSerializer


class DepartamentoSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class ServicioSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer


class LecturaServicioSet(viewsets.ModelViewSet):
    serializer_class = LecturaServicioSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        return LecturaServicio.objects.filter(departamento=departamento)
