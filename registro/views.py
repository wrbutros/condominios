from django.shortcuts import render
from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from rest_framework import viewsets
from .serializers import CondominioSerializer, EdificioSerializer, DepartamentoSerializer, ServicioSerializer, \
    LecturaServicioSerializer


def dashboard(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/dashboard.html', context)


def index(request):
    context = {'latest_question_list': 'jojojo'}
    return render(request, 'registro/index.html', context)


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
    queryset = LecturaServicio.objects.all()
    serializer_class = LecturaServicioSerializer
