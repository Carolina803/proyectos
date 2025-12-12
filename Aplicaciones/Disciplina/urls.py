from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioD, name='inicioD'),
    path('disciplinas/', views.inicioD, name='inicioD'),
    path('disciplinas/nuevo/', views.nuevoD, name='nuevoD'),
    path('disciplinas/guardar/', views.guardarDisciplina, name='guardarDisciplina'),
    path('disciplinas/editar/<int:id>/', views.editarD, name='editarD'),
    path('disciplinas/procesar-edicion/', views.procesarEdicionD, name='procesarEdicionD'),
    path('disciplinas/eliminar/<int:id>/', views.eliminarDisciplina, name='eliminarD'),
]
