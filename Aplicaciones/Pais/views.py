from django.shortcuts import render, redirect, get_object_or_404
from .models import Pais
from django.contrib import messages
from django.db.models.deletion import ProtectedError



def inicioP(request):
    paises = Pais.objects.all()
    return render(request, "inicioP.html", {'paises': paises})


def nuevoP(request):
    return render(request, "nuevoP.html")


def guardarPais(request):
    nombre = request.POST["nombre"]
    if Pais.objects.filter(nombre__iexact=nombre).exists():
        messages.error(request, "❌ El país ya existe")
        return redirect('nuevoP')
    Pais.objects.create(nombre=nombre)
    messages.success(request, "País creado exitosamente")
    return redirect('inicioP')


def editarP(request, id):
        pais = get_object_or_404(Pais, id=id)
        return render(request, "EditarP.html", {'pais': pais})


def procesarEdicionP(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]

    if Pais.objects.filter(nombre__iexact=nombre).exclude(id=id).exists():
        messages.error(request, "❌ El país ya existe")
        return redirect('editarP', id=id)

    pais = get_object_or_404(Pais, id=id)
    pais.nombre = nombre
    pais.save()
    messages.success(request, "País actualizado exitosamente")
    return redirect('inicioP')



def eliminarP(request, id):
        pais = get_object_or_404(Pais, id=id)
        try:
            pais.delete()
            messages.success(request, "País eliminado exitosamente")
        except ProtectedError:
            messages.error(request, "No se puede eliminar el país porque está asociado a deportistas.")
        return redirect('inicioP')
