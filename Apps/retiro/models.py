from django.db import models

# Create your models here.
class retiro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numero_id_pedido = models.CharField(max_length=10)
    telefono = models.CharField(max_length=12)
    mail = models.EmailField()
    

