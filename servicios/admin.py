from django.contrib import admin
from .models import Servicio
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_filter = ("created",('created', DateRangeFilter),"updated",('updated', DateRangeFilter),)
    date_hierarchy = "created"

    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()


admin.site.register(Servicio,ServicioAdmin)
