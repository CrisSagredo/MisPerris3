#from django.contrib.auth.models import Postulante
from rest_framework import serializers
from blog.models import Postulante, Mascota

class PostulanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Postulante
        fields = ('correo', 'rut', 'nombre', 'fechaNacimiento', 'telefono', 'region', 'comuna', 'tipoVivienda', 'fechaPostulacion')

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('foto', 'nombreMascota', 'raza_predominante', 'descripcion', 'estado')

