from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioP, name='inicioP'),
    path('paises/', views.inicioP, name='inicioP'),
    path('paises/nuevo/', views.nuevoP, name='nuevoP'),
    path('paises/guardar/', views.guardarPais, name='guardarPais'),
    path('paises/editar/<int:id>/', views.editarP, name='editarP'),
    path('paises/procesar-edicion/', views.procesarEdicionP, name='procesarEdicionP'),
    path('paises/eliminar/<int:id>/', views.eliminarP, name='eliminarP'),
]
