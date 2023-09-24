from django.urls import path,include, re_path
from django.contrib import admin
from APP.views import mostrar_inicio, PanelLogin, PanelLogout, ClientesCreateView, nosotros, lista_clientes



urlpatterns = [
    path('', mostrar_inicio,name='raiz'),
    path("nosotros", nosotros, name="nosotros"),
    path("login/", PanelLogin.as_view(), name="login"),
    path("logout/", PanelLogout.as_view(), name="logout"),
    path('clientes/create/', ClientesCreateView.as_view(), name ="clientess" ),
    path("clientes/" ,lista_clientes, name="clientes"),
    path('admin/', admin.site.urls),

]
