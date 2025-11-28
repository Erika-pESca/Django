from django.db import models

class Aprendiz(models.Model):
    documento_identidad = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=100, null=True)
    programa_formacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    # Create your models here.
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"