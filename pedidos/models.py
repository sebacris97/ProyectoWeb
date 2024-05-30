from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

User = get_user_model() #esta funcion devuelve el usuario logueado

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    
    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField)
        )["total"]

    def __str__(self):
        return self.id
    
class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="fecha de creacion")
    
    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table='lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Linea Pedidos'
        ordering = ['id']