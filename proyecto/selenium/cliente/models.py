from django.db import models

class Cliente(models.Model):
    codigo = models.CharField(max_length = 8)
    nommbres = models.CharField(max_length = 80)
    apellidos = models.CharField(max_length = 80)
    dni = models.IntegerField(default = 8)

    def __str__(self):
        return f"{self.nommbres} {self.apellidos}"

