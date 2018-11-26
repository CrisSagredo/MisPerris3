from django.conf.urls import url, include
from . import views
#from .views import misPerrisVista, paginaregistro, mascota_view


urlpatterns = [
    url(r'^$', views.misPerrisVista, name='misPerrisVista'),
    url(r'^registro$', views.paginaregistro, name='paginaregistro'),
    url(r'^nuevo$', views.mascota_view, name='mascota_crear'),
    url(r'^perris$', views.perris_estados, name='perris'),
]
