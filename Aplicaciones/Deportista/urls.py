from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioDe, name='inicioDe'),
    path('deportistas/', views.inicioDe, name='inicioDe'),
    path('deportistas/nuevo/', views.nuevoDe, name='nuevoDe'),
    path('deportistas/guardar/', views.guardarDeportista, name='guardarDeportista'),
    path('deportistas/editar/<int:id>/', views.editarDe, name='editarDe'),
    path('deportistas/procesar-edicion/', views.procesarEdicionDe, name='procesarEdicionDe'),
    path('deportistas/eliminar/<int:id>/', views.eliminarDe, name='eliminarDe'),
]
