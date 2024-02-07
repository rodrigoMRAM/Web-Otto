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


class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control',"placeholder":"Nombre"}))
    correo = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',"placeholder":"Email"}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',"placeholder":"Mensaje", 'style': 'resize:none'}))


class TuModeloForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['age']
    def __init__(self, *args, **kwargs):
        super(TuModeloForm, self).__init__(*args, **kwargs)
        self.fields['age'].widget.attrs.update({'id': 'campo'})