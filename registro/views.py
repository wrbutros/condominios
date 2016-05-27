from __future__ import print_function

from rest_framework import mixins
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from models import Condominio, Edificio, Departamento, Servicio, LecturaServicio
from models import AdministradorEdificio, Conserje, MultaEInteres, PagoYAbono
from models import Contrato, Residente, GrupoGasto, Glosa

from serializers import CondominioSerializer, EdificioSerializer
from serializers import DepartamentoSerializer, ServicioSerializer
from serializers import LecturaServicioSerializer, AdministradorEdificioSerializer
from serializers import ConserjeSerializer, MultaEInteresSerializer, ContratoSerializer
from serializers import PagoYAbonoSerializer, DashboardSerializer, ResidenteSerializer
from serializers import GrupoGastoSerializer, GlosaSerializer, RendicionSerializer


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


class MultaEInteresSet(viewsets.ModelViewSet):
    serializer_class = MultaEInteresSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        return MultaEInteres.objects.filter(departamento=departamento)


class PagoYAbonoSet(viewsets.ModelViewSet):
    serializer_class = PagoYAbonoSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        return PagoYAbono.objects.filter(departamento=departamento)


#TODO: Revisar reglas de sobre atributos "activo"
class ResidenteSet(viewsets.ModelViewSet):
    serializer_class = ResidenteSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        #Se busca un residente activo (que viva alli) con contrato vigente
        contrato = Contrato.objects.filter(departamento=departamento,
                                           residente__activo=1,
                                           activo=1)
        idResidente = 0;
        #Si existen 2 contratos (propietario y arriendo) y ambos son vigentes
        #Se busca el arrendatario, de lo contrario se devuelve el propietario
        if len(contrato) > 1:
            for c in contrato:
                if c.tipo == 'A':
                    idRedidente = c.residente.id
        elif len(contrato) == 1:
            idResidente = contrato.first().residente.id

        return Residente.objects.filter(pk=idResidente)


class ContratoSet(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        return Contrato.objects.filter(departamento=departamento)


class GrupoGastoSet(viewsets.ModelViewSet):
    queryset = GrupoGasto.objects.all()
    serializer_class = GrupoGastoSerializer


class GlosaSet(viewsets.ModelViewSet):
    serializer_class = GlosaSerializer

    def get_queryset(self):
        id_condominio = self.kwargs['id_condominio']
        condominio = Condominio.objects.filter(pk=id_condominio)
        return Glosa.objects.filter(condominio=condomino)


# TODO: data debe retornar cada glosa en este formato:
# {
#       "id": "7",
#       "tipoGasto": "REPARACIONES", -----> #GrupoGasto
#       "detalle": "Sueldo Liquidos del Personal",
#       "documento": "Egreso #20",
#       "ingreso": "4790160",
#       "egreso": 0
#},
class RendicionSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RendicionSerializer

    def get_queryset(self):
        id_condominio = self.kwargs['id_condominio']
        condominio = Condominio.objects.filter(pk=id_condominio)
        grupoGasto = GrupoGasto.objects.all()
        glosa = Glosa.objects.filter(condominio=condominio,
                                     fecha__year = datetime.now().year,
                                     fecha__month = datetime.now().month)

        data = [
            {
                "id": "1",
                "tipoGasto": "ADMINISTRACION-REMUNERACIONES",
                "detalle": "Sueldo Liquidos del Personal",
                "documento": "Egreso #20",
                "ingreso": 657300,
                "egreso": 0
            },
            {
                "id": "2",
                "tipoGasto": "ADMINISTRACION-REMUNERACIONES",
                "detalle": "Previred",
                "documento": "Egreso #22",
                "ingreso": 748000,
                "egreso": 0
            },
            {
                "id": "3",
                "tipoGasto": "CONSUMO",
                "detalle": "Articulos de aseo",
                "documento": "Egreso #224",
                "ingreso": "123000",
                "egreso": 0
            },
            {
                "id": "4",
                "tipoGasto": "CONSUMO",
                "detalle": "Previred",
                "documento": "Egreso #22",
                "ingreso": "733654",
                "egreso": 0
            },
            {
                "id": "5",
                "tipoGasto": "MANTENCIONES",
                "detalle": "Sueldo Liquidos del Personal",
                "documento": "Egreso #20",
                "ingreso": "4790160",
                "egreso": 0
            },
            {
                "id": "6",
                "tipoGasto": "MANTENCIONES",
                "detalle": "Previred",
                "documento": "Egreso #22",
                "ingreso": "733654",
                "egreso": 0
            },
            {
                "id": "7",
                "tipoGasto": "REPARACIONES",
                "detalle": "Sueldo Liquidos del Personal",
                "documento": "Egreso #20",
                "ingreso": "4790160",
                "egreso": 0
            },
            {
                "id": "8",
                "tipoGasto": "REPARACIONES",
                "detalle": "Previred",
                "documento": "Egreso #22",
                "ingreso": "733654",
                "egreso": 0
            },
            {
                "id": "9",
                "tipoGasto": "VARIOS",
                "detalle": "Sueldo Liquidos del Personal",
                "documento": "Egreso #20",
                "ingreso": "0",
                "egreso": 5456
            },
            {
                "id": "10",
                "tipoGasto": "VARIOS",
                "detalle": "Previred",
                "documento": "Egreso #22",
                "ingreso": 0,
                "egreso": "733655"
            }
        ];
        return data


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
