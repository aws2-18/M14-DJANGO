from __future__ import unicode_literals

from django.db import models

class Usuarios(models.Model):
	iduser = models.CharField(max_length=10)
	nombreusuario = models.CharField(max_length=20)
	nombre = models.CharField(max_length=10)
	apellidos = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	correo = models.CharField(max_length=30)
	fechanacimiento = models.DateField()
	telefono = models.IntegerField(max_length=9)
	password = models.CharField(max_length=10)
	def __str__(self):
		return self.nombre
	
class Productos(models.Model):
	idproducto = models.CharField(max_length=20)
	nombreproductos = models.CharField(max_length=20)
	cantidad = models.IntegerField(max_length=200)
	precioproducto = models.DecimalField(max_digits=6,decimal_places=2)
	categoria = models.CharField(max_length=20)
	def __str__(self):
		return self.nombreproductos

class Ticket(models.Model):
	usuario = models.ForeignKey(Usuarios)
	producto = models.ForeignKey(Productos)
	preciototal = models.DecimalField(max_digits=6,decimal_places=2)
	
# Create your models here.
