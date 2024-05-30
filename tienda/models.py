from django.db import models

class CategoriaProd(models.Model):
	nombre=models.CharField(max_length=50)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name='Categoria'
		verbose_name_plural='Categorias'
		
	def __str__(self):
		return self.nombre
	
class Producto(models.Model):
	nombre=models.CharField(max_length=50)
	categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
	imagen=models.ImageField(upload_to="tienda", null=True, blank=True,default='default.jpg')
	precio=models.FloatField()
	disponibilidad=models.BooleanField(default=True)
	created=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
	updated=models.DateTimeField(auto_now=True,verbose_name="fecha de actualizacion")

	class Meta:
		verbose_name='Producto'
		verbose_name_plural='Productos'
		
	def __str__(self):
		return self.nombre
