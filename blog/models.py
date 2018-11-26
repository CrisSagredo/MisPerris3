from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Postulante(models.Model):
    correo = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    fechaNacimiento = models.DateTimeField(
            blank=True, null=True)
    telefono = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200)
    tipoVivienda = models.CharField(max_length=200)
    fechaPostulacion = models.DateTimeField(
            default=timezone.now)
            
def publish(self):
    self.fechaPostulacion = timezone.now()
    self.save()

def __str__(self):
    return self.nombre


class Mascota(models.Model):
    foto = models.ImageField()
    nombreMascota = models.CharField(max_length=200)
    raza_predominante = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    ESTADO = (
        ('disponible', 'Disponible'),
        ('adoptado', 'Adoptado'),
        ('rescatado', 'Rescatado'),
    )
    estado = models.TextField(choices = ESTADO)

""" Para borrar de /media/ las fotos que no son usadas por ninguna clase """
@receiver(post_delete, sender=Mascota)
def submission_delete(sender, instance, **kwargs):
    instance.foto.delete(False)