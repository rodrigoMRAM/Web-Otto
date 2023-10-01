from django.urls import path,include, re_path
from django.contrib import admin
from APP.views import mostrar_inicio, PanelLogin, PanelLogout, ClientesCreateView, nosotros, lista_clientes , delete, ClienteUpdate, filtro,UserDetalle,UserUpdate,cambiar_contraseña,UserLogout



urlpatterns = [
    path('', mostrar_inicio,name='raiz'),
    path("nosotros", nosotros, name="nosotros"),
    path("login/", PanelLogin.as_view(), name="login"),
    path("logout/", PanelLogout.as_view(), name="logout"),
    path('clientes/create/', ClientesCreateView.as_view(), name ="clientess" ),
    path("clientes/" ,lista_clientes, name="clientes"),
    path("delete/<id>" , delete, name="eliminar"),
    path('admin/', admin.site.urls),
    path(r'^editar/(?P<pk>\d+)$', ClienteUpdate.as_view(), name="editar"),
    path('filtro/', filtro, name='filtro'),
    path("userUpdate/<pk>/" , UserDetalle.as_view(), name="userUpdate"),
    path("actualizacion/<pk>/edit", UserUpdate.as_view(), name="editarusuario"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("cambiarPass/", cambiar_contraseña, name="cambiarPass" )


]
