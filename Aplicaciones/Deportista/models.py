from django.db import models
from Aplicaciones.Pais.models import Pais
from Aplicaciones.Disciplina.models import Disciplina

class Deportista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estatura_cm = models.SmallIntegerField(null=True, blank=True)
    peso_kg = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre
