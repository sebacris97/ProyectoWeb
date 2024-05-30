from django.contrib import admin
from .models import Categoria, Post

from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_filter = ("created",('created', DateRangeFilter),"updated",('updated', DateRangeFilter),)
    date_hierarchy = "created"
	
    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()

admin.site.register(Post,PostAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_filter = ("created",('created', DateRangeFilter),"updated",('updated', DateRangeFilter),)
    date_hierarchy = "created"
	
    def get_readonly_fields(self, request, obj=None): #ocultar readonlys en el add de admin
        if obj: # Editing
            return self.readonly_fields
        return ()

admin.site.register(Categoria,CategoriaAdmin)

