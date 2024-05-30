from django.contrib import admin

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

from pedidos.models import Pedido,LineaPedido

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_filter = ("created_at",('created_at', DateRangeFilter))
    date_hierarchy = "created_at"
	
    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()
    
"""class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_filter = ("created_at",('created_at', DateRangeFilter))
    date_hierarchy = "created_at"
	
    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()"""

admin.site.register([Pedido,LineaPedido])