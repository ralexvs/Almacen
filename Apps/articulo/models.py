from django.db import models
from Apps.retiro.models import retiro

# Create your models here.
class accesorio(models.Model):
    tipo = models.CharField(max_length=60)

class articulo(models.Model):
    tipo_articulo = models.CharField(max_length=60)
    talla = models.CharField(max_length=3)
    color = models.CharField(max_length=20)
    fecha_llegada = models.DateField()
    retiro = models.ForeignKey(retiro, null=False, blank=True, on_delete=models.CASCADE)
    accesorio = models.ManyToManyField(accesorio)


