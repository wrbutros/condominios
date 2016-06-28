from __future__ import print_function

from datetime import datetime

from rest_framework import mixins
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
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


@csrf_exempt
def residenteForm(request, id_condominio):
    residente = Residente (
        rut = request.POST['rut'],
        nombres = request.POST['nombres'],
        apellido_paterno = request.POST['apellido_paterno'],
        apellido_materno = request.POST['apellido_materno'],
        genero = request.POST['genero'],
        fono = request.POST['fono'],
        email = request.POST['email'],
        fecha_ingreso = request.POST['fecha_ingreso'],
        activo = request.POST['activo'])

    residente.save()
    return JsonResponse({'action': 'add',
                         'status': 'ok'})


@csrf_exempt
def jqgrid(request, id_condominio):
    oper = request.POST['oper']

    if oper == "add":
        condominio = Condominio.objects.get(pk=id_condominio)
        grupoGasto = GrupoGasto.objects.get(pk=request.POST['tipoGasto'])
        glosa = Glosa (
            nombre = request.POST['nombre'],
            grupoGasto = grupoGasto,
            condominio = condominio,
            descripcion = request.POST['descripcion'],
            nombreDocumentoOrig = request.POST['documento'],
            fecha = datetime.now(),
            ingreso = request.POST['ingreso'],
            egreso = request.POST['egreso'])
        glosa.save()

        return JsonResponse({'action': oper,
                             'status': 'ok'})
    elif oper == "edit":
        condominio = Condominio.objects.get(pk=id_condominio)
        grupoGasto = GrupoGasto.objects.get(pk=request.POST['tipoGasto'])

        glosa = Glosa.objects.get(pk=request.POST['id'])
        glosa.nombre = request.POST['nombre']
        glosa.grupoGasto = grupoGasto
        glosa.condominio = condominio
        glosa.descripcion = request.POST['descripcion']
        glosa.nombreDocumentoOrig = request.POST['documento']
        glosa.fecha = datetime.now()
        glosa.ingreso = request.POST['ingreso']
        glosa.egreso = request.POST['egreso']
        glosa.save()

        return JsonResponse({'action': oper,
                             'status': 'ok'})
    elif oper == "del":
        Glosa.objects.filter(pk=request.POST['id']).delete()

        return JsonResponse({'action': oper,
                             'status': 'ok'})


class ConserjeSet(viewsets.ModelViewSet):
    queryset = Conserje.objects.all()
    serializer_class = ConserjeSerializer


class AdministradorEdificioSet(viewsets.ModelViewSet):
    queryset = AdministradorEdificio.objects.all()
    serializer_class = AdministradorEdificioSerializer


class ResidenteSet(viewsets.ModelViewSet):
    queryset = Residente.objects.all()
    serializer_class = ResidenteSerializer


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


class LecturaServicioCondominioSet(viewsets.ModelViewSet):
    serializer_class = LecturaServicioSerializer

    def get_queryset(self):
        id_condominio = self.kwargs['id_condominio']
        condominio = Condominio.objects.filter(pk=id_condominio)
        return LecturaServicio.objects.filter(departamento__edificio__condominio__id=condominio.first().id)


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


# TODO: Revisar reglas de sobre atributos "activo"
class ResidenteActualSet(viewsets.ModelViewSet):
    serializer_class = ResidenteSerializer

    def get_queryset(self):
        id_departamento = self.kwargs['id_departamento']
        departamento = Departamento.objects.filter(pk=id_departamento)
        # Se busca un residente activo (que viva alli) con contrato vigente
        contrato = Contrato.objects.filter(departamento=departamento,
                                           residente__activo=1,
                                           activo=1)
        idResidente = 0;
        # Si existen 2 contratos (propietario y arriendo) y ambos son vigentes
        # Se busca el arrendatario, de lo contrario se devuelve el propietario
        if len(contrato) > 1:
            for c in contrato:
                if c.tipo == 'A':
                    idRedidente = c.residente.id
        elif len(contrato) == 1:
            idResidente = contrato.first().residente.id

        return Residente.objects.filter(pk=idResidente)


class ContratoCondominioSet(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer

    def get_queryset(self):
        id_condominio = self.kwargs['id_condominio']
        condominio = Departamento.objects.filter(pk=id_condominio)
        return Contrato.objects.filter(departamento__edificio__condominio__id=condominio.first().id)


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
        return Glosa.objects.filter(condominio=condominio)


class RendicionSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RendicionSerializer

    def get_queryset(self):
        id_condominio = self.kwargs['id_condominio']
        condominio = Condominio.objects.filter(pk=id_condominio)
        gruposGasto = GrupoGasto.objects.all()
        glosas = Glosa.objects.filter(condominio=condominio,
                                      fecha__year=datetime.now().year,
                                      fecha__month=datetime.now().month)

        # Its making the 'glosa' JSON
        data = []
        for glosa in glosas:
            data.append(
                {
                    "id": str(glosa.id),
                    "tipoGasto": glosa.grupoGasto.nombre,
                    "nombre": glosa.nombre,
                    "descripcion": glosa.descripcion,
                    "documento": glosa.nombreDocumentoOrig,
                    "ingreso": glosa.ingreso,
                    "egreso": glosa.egreso
                }
            )
        # Se genera el String con todos los grupo gastos disponibles
        stringGrupos = ""
        for grupo in gruposGasto:
            if stringGrupos != "":
                stringGrupos += ";"
            stringGrupos += str(grupo.id) + ":" + grupo.nombre

        result = [{
            "data": data,
            "grupos": stringGrupos
        }]

        return result


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
                "Julio",
                "Agosto",
                "Septiembre",
                "Octubre",
                "Noviembre",
                "Diciembre"
            ],
            "data": [
                11456789,
                12456734,
                14475637,
                13456321,
                14567432,
                15543876,
                15345687,
                14567432,
                15456321,
                15875637,
                15456734,
                16456789,
            ]
        }]
