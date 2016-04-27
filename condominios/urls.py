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
from registro.views import ServicioSet, LecturaServicioSet
from geoname.views import CiudadSet, ComunaSet

router = routers.DefaultRouter()
router.register(r'v1/ciudades', CiudadSet)
router.register(r'comunas', ComunaSet)
router.register(r'administradores', AdministradorEdificioSet)
router.register(r'conserjes', ConserjeSet)
router.register(r'condominios', CondominioSet)
router.register(r'edificios', EdificioSet, 'edificios')
router.register(r'departamentos', DepartamentoSet, 'departamentos')
router.register(r'serviciostypes', ServicioSet, 'serviciostypes')

router.register(r'departamentos/(?P<id_departamento>.+)/servicios', LecturaServicioSet, 'servicios')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^condominios/', include('registro.urls')),
]
