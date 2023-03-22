from django.db import models

# Create your models here.

class Post(models.Model):
    Nombre= models.CharField(max_length=30)
    Apellido= models.CharField(max_length=80)
    DNI= models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id} - {self.Nombre}"
    

class Busqueda_Curso(models.Model):
    Curso= models.CharField(max_length=30)
    Camada= models.CharField(max_length=80)

    def __str__(self):
        return f"{self.id} - {self.Curso}"
    
class Datos(models.Model):
    Pais= models.CharField(max_length=30)
    fecha_de_nacimiento= models.CharField(max_length=80)

    def __str__(self):
        return f"{self.id} - {self.Pais}"
    