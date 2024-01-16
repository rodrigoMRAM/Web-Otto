from django.http import JsonResponse
from django.shortcuts import render, redirect
from APP.forms import Datos
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView , View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from APP.forms import CustomAuthenticationForm
from django.urls import reverse_lazy
from .models import *
from .filters import ListingFilter
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, TuModeloForm
from django.core.mail import send_mail

# Create your views here.
# def mostrar_inicio(request):
#     return render(request,"APP/index.html",{})
def mostrar_inicio(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            mensaje_completo = f"De: {nombre}\nCorreo: {correo}\n\nMensaje:\n{mensaje}"

            send_mail(
                'Mensaje desde el formulario de contacto',  # Asunto del correo
                mensaje_completo,
                correo,  # Dirección de correo del remitente
                ['rodrigomacielth@gmail.com'],  # Dirección de correo del destinatario
                fail_silently=False,
            )
            return redirect('raiz')  # Página de éxito después de enviar el formulario

    else:
        form = ContactForm()

    return render(request, "APP/index.html", {'form': form})

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

#EDITAR DATOS DE CLIENTES
# class ClientesCreateView(LoginRequiredMixin, CreateView):
#     model = Clientes
#     fields = ['nombre', 'patente',"mes","dia","age", "detalles", "total"]
#     template_name = "APP/clientes_form.html"
#     success_url = reverse_lazy("raiz")

#LISTA DE CLIENTES (PAGINA PRINCIPAL DE USUARIO)
@login_required
def lista_clientes(request):
    if request.method == "POST":
        formulario = Datos(request.POST)
        print(formulario)
        if formulario.is_valid:
            datos = formulario.cleaned_data
            nombreMayus = ' '.join(word.capitalize() for word in datos["nombre"].split())
            cliente = Clientes(nombre=nombreMayus,patente=datos["patente"], mes=datos["mes"],dia=datos["dia"],age=datos["age"],detalles=datos["detalles"],total=datos["total"])
            cliente.save()
            clientes = Clientes.objects.all().order_by('-id')
            formulario = Datos()
            # FUNCION DE BARRAS
           


            return render(request, "APP/clientes.html",{"datos":datos, "formulario" : formulario , "clientes":clientes})
    else:
        formulario = Datos()

        # FUNCION DE SUMAR TOTAL PARA DEVOLVERLO A LA BARRA DE NIVELES
        final = Clientes.objects.filter(mes='Septiembre').values_list('total', flat=True)
        print(final)
        for x in final:
            resultado = 0
            final1 = resultado + x
            print(final1)

        clientes = Clientes.objects.all().order_by('-id')


    return render(request, "APP/clientes.html",{"formulario":formulario,"clientes":clientes})


@login_required
def delete(request, id):
     eliminar = Clientes.objects.get(id=id)
     eliminar.delete()
     return redirect('clientes')

#ELIMINAR CLIENTE
class ClientesDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes 
    success_url = reverse_lazy('clientes')



# EDITAR CLIENTE
class ClienteUpdate(UpdateView):

    model = Clientes
    success_url = "/clientes/"
    fields = ['nombre', 'patente',"mes","dia","age", "detalles", "total"]



# FILTRO
@login_required
def filtro(request):
    clientes = Clientes.objects.all().order_by('-id')
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

#LOGOUT

class UserLogout(LogoutView):
    template_name = 'APP/index.html'
# CAMBIAR CONTRASEÑA
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


#ECHART FUNCION
@login_required
def api(request):
    if request.method == 'POST':
        form1 = TuModeloForm(request.POST)
        if form1.is_valid():
            valor_seleccionado = form1.cleaned_data['age']
            datos = Clientes.MESES
            enero = list(Clientes.objects.filter(mes='Enero' ,age =valor_seleccionado).values_list('total', flat=True))
            febrero = list(Clientes.objects.filter(mes='Febrero',age =valor_seleccionado).values_list('total', flat=True))
            marzo = list(Clientes.objects.filter(mes='Marzo',age =valor_seleccionado).values_list('total', flat=True))
            abril = list(Clientes.objects.filter(mes='Abril',age =valor_seleccionado).values_list('total', flat=True))
            mayo = list(Clientes.objects.filter(mes='Mayo',age =valor_seleccionado).values_list('total', flat=True))
            junio = list(Clientes.objects.filter(mes='Junio',age =valor_seleccionado).values_list('total', flat=True))
            julio = list(Clientes.objects.filter(mes='Julio',age =valor_seleccionado).values_list('total', flat=True))
            agosto = list(Clientes.objects.filter(mes='Agosto',age =valor_seleccionado).values_list('total', flat=True))
            septiembre = list(Clientes.objects.filter(mes='Septiembre',age =valor_seleccionado).values_list('total', flat=True))
            octubre = list(Clientes.objects.filter(mes='Octubre',age =valor_seleccionado).values_list('total', flat=True))
            noviembre = list(Clientes.objects.filter(mes='Noviembre',age =valor_seleccionado).values_list('total', flat=True))
            diciembre = list(Clientes.objects.filter(mes='Diciembre',age =valor_seleccionado).values_list('total', flat=True))
            xa = []
            numero = 0
            meses = [enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]

            for x in meses:
                if len(x) == 0:
                    xa.append(0)
                else:
                    for y in x:   
                        numero = numero+y
                    xa.append(numero)
            form = TuModeloForm()
            context = {'data': "Success",'datos' : datos, 'xa': xa ,'form' :form}
            return render(request, 'APP/echartAjax.html', context)
    else:

        form = TuModeloForm()


    return render(request, 'APP/echartAjax.html', {'form': form })


# def incomesAverage(request):
#         datos = Clientes.MESES
#         enero = list(Clientes.objects.filter(mes='Enero').values_list('total', flat=True))
#         febrero = list(Clientes.objects.filter(mes='Febrero').values_list('total', flat=True))
#         marzo = list(Clientes.objects.filter(mes='Marzo').values_list('total', flat=True))
#         abril = list(Clientes.objects.filter(mes='Abril').values_list('total', flat=True))
#         mayo = list(Clientes.objects.filter(mes='Mayo').values_list('total', flat=True))
#         junio = list(Clientes.objects.filter(mes='Junio').values_list('total', flat=True))
#         julio = list(Clientes.objects.filter(mes='Julio').values_list('total', flat=True))
#         agosto = list(Clientes.objects.filter(mes='Agosto').values_list('total', flat=True))
#         septiembre = list(Clientes.objects.filter(mes='Septiembre').values_list('total', flat=True))
#         octubre = list(Clientes.objects.filter(mes='Octubre').values_list('total', flat=True))
#         noviembre = list(Clientes.objects.filter(mes='Noviembre').values_list('total', flat=True))
#         diciembre = list(Clientes.objects.filter(mes='Diciembre').values_list('total', flat=True))
#         xa = []
#         numero = 0

#         meses = [enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre]

#         for x in meses:
#             if len(x) == 0:
#                 xa.append(0)
#             else:
#                 for y in x:   
#                     numero = numero+y
#                 xa.append(numero)
        
#         context = {'data': "Success",'datos' : datos, 'xa': xa}
#         return JsonResponse(context)
