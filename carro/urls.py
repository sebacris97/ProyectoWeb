"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name="carro"

urlpatterns = [
    path("agregar/<int:producto_id>",views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>",views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>",views.restar_producto, name="restar"),
    path("limpiar/<int:producto_id>",views.limpiar_carro, name="limpiar"),
]
