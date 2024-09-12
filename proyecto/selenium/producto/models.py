from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length = 8)
    nombre = models.CharField(max_length = 80)
    descripcion = models.CharField(max_length = 200)
    precio = models.IntegerField(default = 0)

    def __str__(self):
        return f"{self.codigo} {self.nombre}"
