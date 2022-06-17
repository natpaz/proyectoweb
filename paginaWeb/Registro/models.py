from django.db import models

# Acá creamos nuestros modelos a utilizar para la página. Con cliente nos referimos a usuario.
class Formulario(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje =models.TextField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    formulario = models.ForeignKey(Formulario, null=True, blank=True, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    domicilio = models.TextField()
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre