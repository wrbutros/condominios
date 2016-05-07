from __future__ import print_function

from rest_framework import mixins
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import AdministradorEdificio, Conserje

from serializers import CondominioSerializer, EdificioSerializer
from serializers import DepartamentoSerializer, ServicioSerializer
from serializers import LecturaServicioSerializer, AdministradorEdificioSerializer
from serializers import ConserjeSerializer, DashboardSerializer


def dashboard(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/dashboard.html', context)


def index(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/index.html', context)


class ConserjeSet(viewsets.ModelViewSet):
    queryset = Conserje.objects.all()
    serializer_class = ConserjeSerializer


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


class DashboardSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = DashboardSerializer

    def get_queryset(self):
        return [{
            "nombre": "Otros tulipanes",
            "labels": [
                "Enero",
                "Febrero",
                "Marzo",
                "Abril",
                "Mayo",
                "Junio",
                "Julio"
            ],
            "data": [
                11456789,
                12456734,
                15475637,
                13456321,
                14567432,
                16543876,
                19345687
            ]
        }]
