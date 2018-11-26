from django import forms
from .models import Mascota
from .models import Postulante

years = [x for x in range(1900, 2018)]
estado = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),('Option 3', 'Option 3'))

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'foto',
            'nombreMascota',
            'raza_predominante',
            'descripcion',
            'estado',

        ]
        labels = {
            'foto' : 'Foto del Perro',
            'nombreMascota': 'Nombre',
            'raza_predominante' : 'Raza predominante',
            'descripcion' : 'Descripcion',
            'estado' : 'Estado',

        }
        widgets = {
            'foto': forms.TextInput(attrs={'class':'form-control'}),
            'nombreMascota': forms.TextInput(attrs={'class':'form-control'}),
            'raza_predominante': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.Select(choices=estado,attrs={'class':'form-control'}),
        }

class PostulanteForm(forms.ModelForm):

    class Meta:
        
        model = Postulante

        fields = [
            'correo',
            'rut',
            'nombre',
            'fechaNacimiento',
            'telefono',
            'region',
            'comuna',
            'tipoVivienda',
            'fechaPostulacion',

        ]
        labels = {
            'correo' : 'Correo',
            'rut' : 'RUT',
            'nombre' : 'Nombre',
            'fechaNacimiento' : 'Fecha de Nacimiento',
            'telefono' : 'Número de Teléfono',
            'region' : 'Región',
            'comuna' : 'Comuna',
            'tipoVivienda' : 'Tipo de Vivienda',
            'fechaPostulacion' : 'Fecha de Postulación',
        }
        widgets = {
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'fechaNacimiento': forms.SelectDateWidget(years=years,attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'region': forms.TextInput(attrs={'class':'form-control'}),
            'comuna': forms.TextInput(attrs={'class':'form-control'}),
            'tipoVivienda': forms.TextInput(attrs={'class':'form-control'}),
            'fechaPostulacion': forms.SelectDateWidget(attrs={'class':'form-control'}),
        }