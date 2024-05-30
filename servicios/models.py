from django.db import models

# Create your models here.

class Servicio(models.Model):
	titulo=models.CharField(max_length=51)
	contenido=models.CharField(max_length=50)
	imagen=models.ImageField(upload_to='servicios',blank=True,null=True,default="default.jpg")
	created=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
	updated=models.DateTimeField(auto_now=True,verbose_name="fecha de actualizacion")
	
	class Meta:
		verbose_name='servicio'
		verbose_name_plural='servicios'
		
	def __str__(self):
		return self.titulo
