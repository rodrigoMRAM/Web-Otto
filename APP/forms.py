from django.contrib.auth.forms import AuthenticationForm
from django import forms
from APP.models import Clientes


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=None, *args, **kwargs)
        self.fields['username'].label = 'Usuario'
        self.fields['password'].label = 'Contraseña'


class Datos(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'