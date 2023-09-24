from django.shortcuts import render
from APP.forms import Datos
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from APP.forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from APP.models import Clientes

# Create your views here.
def mostrar_inicio(request):
    return render(request,"APP/index.html",{})

def nosotros(request):
    return render(request, "APP/nosotros.html")
# VIEWS DE LOGIN
class PanelLogin(LoginView):
    template_name = "APP/login.html"
    next_page = reverse_lazy("raiz")
    authentication_form = CustomAuthenticationForm
# VIEWS DE LOGOUT
class PanelLogout(LogoutView):
    template_name = 'APP/index.html'

class ClientesCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = ['nombre' ,'patente', 'fechaDeIngreso', 'detalles','total']
    template_name = "APP/clientes_form.html"
    success_url = reverse_lazy("raiz")


def lista_clientes(request):
    if request.method == "POST":
        formulario = Datos(request.POST)
        print(formulario)
        if formulario.is_valid:
            datos = formulario.cleaned_data
            cliente = Clientes(nombre=datos["nombre"],patente=datos["patente"], fechaDeIngreso=datos["fechaDeIngreso"],detalles=datos["detalles"],total=datos["total"])
            cliente.save()
            clientes = Clientes.objects.all()
            formulario = Datos()
            return render(request, "APP/clientes.html",{"datos":datos, "formulario" : formulario , "clientes":clientes})
    else:
        formulario = Datos()
        clientes = Clientes.objects.all()


    return render(request, "APP/clientes.html",{"formulario":formulario,"clientes":clientes})