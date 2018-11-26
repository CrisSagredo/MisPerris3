from django.shortcuts import render, redirect
from .forms import MascotaForm, PostulanteForm
from .models import Mascota
#from django.http import HttpResponse


# Create your views here.
def misPerrisVista(request):
    template = 'blog/misPerrisVista.html'
    return render(request, template, {})

def paginaregistro(request):
    if request.method == 'POST':
        form = PostulanteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('https://127.0.0.1:8000/')
    else:
        form = PostulanteForm()
    return render(request, 'blog/paginaregistro.html', {'form':form})


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('https://127.0.0.1:8000/registro')
    else:
        form = MascotaForm()
    return render(request, 'blog/mascota_form.html', {'form':form})

def perris_estados(request):
    forms = Mascota.objects.all()
    return render(request, 'blog/perris_estados.html', {'forms':forms})

