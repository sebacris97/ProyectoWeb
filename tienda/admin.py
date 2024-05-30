from django.contrib import admin
from .models import CategoriaProd, Producto
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_filter = ("created",('created', DateRangeFilter),"updated",('updated', DateRangeFilter),)
    date_hierarchy = "created"

    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()


admin.site.register(CategoriaProd,CategoriaProdAdmin)

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_filter = (('categorias', RelatedDropdownFilter),"created",('created', DateRangeFilter),"updated",('updated', DateRangeFilter),)
    date_hierarchy = "created"

    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()


admin.site.register(Producto,ProductoAdmin)

