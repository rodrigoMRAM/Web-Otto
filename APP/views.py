from django.shortcuts import render, redirect
from APP.forms import Datos
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView , View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from APP.forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from APP.models import Clientes
from .filters import ListingFilter
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def mostrar_inicio(request):
    return render(request,"APP/index.html",{})

def nosotros(request):
    return render(request, "APP/nosotros.html")
# VIEWS DE LOGIN
class PanelLogin(LoginView):
    template_name = "APP/login.html"
    next_page = reverse_lazy("clientes")
    authentication_form = CustomAuthenticationForm
# VIEWS DE LOGOUT
class PanelLogout(LogoutView):
    template_name = 'APP/index.html'

class ClientesCreateView(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = ['nombre' ,'patente', 'fechaDeIngreso', 'detalles','total']
    template_name = "APP/clientes_form.html"
    success_url = reverse_lazy("raiz")

@login_required
def lista_clientes(request):
    if request.method == "POST":
        formulario = Datos(request.POST)
        print(formulario)
        if formulario.is_valid:
            datos = formulario.cleaned_data
            cliente = Clientes(nombre=datos["nombre"],patente=datos["patente"], mes=datos["mes"],dia=datos["dia"],age=datos["age"],detalles=datos["detalles"],total=datos["total"])
            cliente.save()
            clientes = Clientes.objects.all()
            formulario = Datos()


            return render(request, "APP/clientes.html",{"datos":datos, "formulario" : formulario , "clientes":clientes})
    else:
        formulario = Datos()
        clientes = Clientes.objects.all()


    return render(request, "APP/clientes.html",{"formulario":formulario,"clientes":clientes})

@login_required
def delete(request, id):
     eliminar = Clientes.objects.get(id=id)
     eliminar.delete()
     return redirect('clientes')




class ClienteUpdate(UpdateView):

    model = Clientes
    success_url = "/clientes/"
    fields = ['nombre', 'patente',"fechaDeIngreso", "detalles", "total"]



# FILTRO
@login_required
def filtro(request):
    clientes = Clientes.objects.all()
    listing_filter = ListingFilter(request.GET , queryset=clientes)
    context = {
        'listing_filter': listing_filter
    }
    return render(request,'APP/filtro.html', context)



class UserUpdate(UpdateView):

    model = User
    success_url = "/userlist/"
    fields = ['username', 'email', 'last_name', 'first_name']

class UserDetalle(DetailView):

    model = User
    template_name ="APP/user_detail.html"



class UserLogout(LogoutView):
    template_name = 'APP/index.html'

@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Contraseña cambiada con éxito.')
            # Redirigir a una página de confirmación o a donde desees.
            return redirect('clientes')
        else:
            messages.error(request, 'Error al cambiar la contraseña. Por favor, corrija los errores.')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'APP/cambiarPass.html', {'form': form})