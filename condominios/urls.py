"""condominios URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from registro.views import AdministradorEdificioSet, ConserjeSet
from registro.views import CondominioSet, EdificioSet, DepartamentoSet
from registro.views import ServicioSet, LecturaServicioSet, DashboardSet
from registro.views import PagoYAbonoSet, MultaEInteresSet, ContratoSet
from registro.views import ResidenteSet, GrupoGastoSet, GlosaSet

from geoname.views import CiudadSet, ComunaSet

router = routers.DefaultRouter()
router.register(r'v1/ciudades', CiudadSet)
router.register(r'v1/comunas', ComunaSet)
router.register(r'v1/administradores', AdministradorEdificioSet)
router.register(r'v1/conserjes', ConserjeSet)

router.register(r'v1/condominios', CondominioSet)
router.register(r'v1/condominios/(?P<id_condominio>.+)/dashboard', DashboardSet, 'dashboard')
#router.register(r'v1/condominios/(?P<id_condominio>.+)/dashboard', DashboardSet, 'dashboard')

router.register(r'v1/edificios', EdificioSet, 'edificios')
router.register(r'v1/departamentos', DepartamentoSet, 'departamentos')
router.register(r'v1/serviciostypes', ServicioSet, 'serviciostypes')
router.register(r'v1/grupoGastos', GrupoGastoSet, 'grupogastos')

# NOTE: This url is not show in API browser
router.register(r'v1/departamentos/(?P<id_departamento>.+)/servicios', LecturaServicioSet, 'servicios')
router.register(r'v1/departamentos/(?P<id_departamento>.+)/pagosyabonos', PagoYAbonoSet, 'pagosYAbonos')
router.register(r'v1/departamentos/(?P<id_departamento>.+)/multaseintereses', MultaEInteresSet, 'multasEIntereses')
router.register(r'v1/departamentos/(?P<id_departamento>.+)/contratos', ContratoSet, 'contratos')
router.register(r'v1/departamentos/(?P<id_departamento>.+)/residenteactual', ResidenteSet, 'residente')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^condominios/', include('registro.urls')),
]
