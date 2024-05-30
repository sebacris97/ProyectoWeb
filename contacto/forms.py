from django import forms

class FormularioContacto(forms.Form):
    asunto = forms.CharField(label='Asunto' , required=True)
    email = forms.EmailField(label='Email' , required=True)
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'style':'resize:none;'}))
    