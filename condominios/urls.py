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
from registro import views

router = routers.DefaultRouter()
router.register(r'v1/ciudades', views.CiudadSet)
router.register(r'comunas', views.ComunaSet)
router.register(r'administradores', views.AdministradorEdificioSet)
router.register(r'conserjes', views.ConserjeSet)
router.register(r'condominios', views.CondominioSet)
router.register(r'edificios', views.EdificioSet, 'edificios')
router.register(r'departamentos', views.DepartamentoSet, 'departamentos')
router.register(r'serviciostypes', views.ServicioSet, 'serviciostypes')

router.register(r'departamentos/(?P<id_departamento>.+)/servicios', views.LecturaServicioSet, 'servicios')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^condominios/', include('registro.urls')),
]
