from django.contrib.auth.forms import AuthenticationForm
from django import forms
from APP.models import Clientes
from django.forms import ModelForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'


class Datos(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'


class MiModeloForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']

    # Cambia la etiqueta del campo en el formulario
    username = forms.CharField(label='Usuario')

