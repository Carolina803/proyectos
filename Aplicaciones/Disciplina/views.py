from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from .models import Disciplina


def inicioD(request):
    disciplinas = Disciplina.objects.all()
    return render(request, "inicioD.html", {'disciplinas': disciplinas})


def nuevoD(request):
    return render(request, "nuevoD.html")


def guardarDisciplina(request):
    nombre = request.POST["nombre"]
    if Disciplina.objects.filter(nombre__iexact=nombre).exists():
        messages.error(request, "❌ La disciplina ya existe")
        return redirect('nuevoD')
    Disciplina.objects.create(nombre=nombre)
    messages.success(request, "Disciplina creada exitosamente")
    return redirect('inicioD')




def editarD(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    return render(request, "EditarD.html", {'disciplina': disciplina})


def procesarEdicionD(request):
    id = request.POST["id"]
    nombre = request.POST["nombre"]

    if Disciplina.objects.filter(nombre__iexact=nombre).exclude(id=id).exists():
        messages.error(request, "❌ La disciplina ya existe")
        return redirect('editarD', id=id)

    disciplina = get_object_or_404(Disciplina, id=id)
    disciplina.nombre = nombre
    disciplina.save()
    messages.success(request, "Disciplina actualizada exitosamente")
    return redirect('inicioD')



def eliminarDisciplina(request, id):
    disciplina = get_object_or_404(Disciplina, id=id)
    try:
        disciplina.delete()
        messages.success(request, "Disciplina eliminada exitosamente")
    except ProtectedError:
        messages.error(
            request,
            "No se puede eliminar la disciplina porque está asociada a deportistas."
        )
    return redirect('inicioD')
