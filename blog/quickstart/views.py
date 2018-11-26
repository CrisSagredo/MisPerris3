#from django.contrib.auth.models import Postulante
from rest_framework import viewsets
from blog.quickstart.serializers import PostulanteSerializer, MascotaSerializer
from blog.models import Postulante, Mascota


class PostulanteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Postulante.objects.all().order_by('fechaNacimiento')
    serializer_class = PostulanteSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Mascota.objects.all().order_by('estado')
    serializer_class = MascotaSerializer

