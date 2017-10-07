from django.db import models

tipos = ['Perro','Gato']

class Mascota(models.Model):
	tipo = models.CharField(max_length=200)
	def __str__(self):
		return self.tipo

class Color(models.Model):
	color = models.CharField(max_length=100)
	def __str__(self):
		return self.color

class Animal(models.Model):
	nombre = models.CharField(max_length=200)
	tipo = models.ForeignKey(Mascota, on_delete=models.CASCADE)
	fecha_publicacion = models.DateTimeField('fecha publicacion')
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	peso = models.IntegerField(default=0)
	descripcion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

# Create your models here.
