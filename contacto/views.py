from django.shortcuts import redirect, render
from .forms import FormularioContacto
from ProyectoWeb.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def contacto(request):
    if request.method=="POST":
        formulario=FormularioContacto(request.POST)
        if formulario.is_valid():
            inform = formulario.cleaned_data
            try:
                send_mail(inform['asunto'],inform['message'],EMAIL_HOST_USER,[inform.get('email','')])
                return redirect("/contacto/?valido")
                #return render(request, "contacto/gracias.html")
            except:
                return redirect("/contacto/?novalido")
    else:
        formulario=FormularioContacto()
    return render(request, "contacto/contacto.html", {'form':formulario})

