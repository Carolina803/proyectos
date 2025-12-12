from django.shortcuts import render, redirect
from .models import Deportista
from Aplicaciones.Pais.models import Pais
from Aplicaciones.Disciplina.models import Disciplina
from django.contrib import messages

def inicioDe(request):
    deportistas = Deportista.objects.all()
    return render(request, "inicioDe.html", {'deportistas': deportistas})

def nuevoDe(request):
    paises = Pais.objects.all()
    disciplinas = Disciplina.objects.all()
    return render(request, "nuevoDe.html", {'paises': paises, 'disciplinas': disciplinas})

def guardarDeportista(request):
    nombre = request.POST["nombre"]
    pais = request.POST["pais"]
    disciplina = request.POST["disciplina"]
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    estatura_cm = request.POST.get("estatura_cm")
    peso_kg = request.POST.get("peso_kg")

    if Deportista.objects.filter(nombre__iexact=nombre).exists():
        messages.error(request, "❌ El deportista ya existe")
        return redirect('nuevoDe')

    Deportista.objects.create(
        nombre=nombre,
        pais_id=pais,
        disciplina_id=disciplina,
        fecha_nacimiento=fecha_nacimiento,
        estatura_cm=estatura_cm,
        peso_kg=peso_kg
    )
    messages.success(request, "Deportista creado exitosamente")
    return redirect('inicioDe')


def editarDe(request, id):
    deportista = Deportista.objects.get(id=id)
    paises = Pais.objects.all()
    disciplinas = Disciplina.objects.all()
    return render(request, "EditarDe.html", {'deportista': deportista, 'paises': paises, 'disciplinas': disciplinas})

def procesarEdicionDe(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]
    pais = request.POST["pais"]
    disciplina = request.POST["disciplina"]
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    estatura_cm = request.POST.get("estatura_cm")
    peso_kg = request.POST.get("peso_kg")

    if Deportista.objects.filter(nombre__iexact=nombre).exclude(id=id).exists():
        messages.error(request, "❌ El deportista ya existe")
        return redirect('editarDe', id=id)

    deportista = Deportista.objects.get(id=id)
    deportista.nombre = nombre
    deportista.pais_id = pais
    deportista.disciplina_id = disciplina
    deportista.fecha_nacimiento = fecha_nacimiento
    deportista.estatura_cm = estatura_cm
    deportista.peso_kg = peso_kg
    deportista.save()

    messages.success(request, "Deportista actualizado exitosamente")
    return redirect('inicioDe')


def eliminarDe(request, id):
    deportista = Deportista.objects.get(id=id)
    deportista.delete()
    messages.success(request, "Deportista eliminado exitosamente")
    return redirect('inicioDe')
