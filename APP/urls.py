from django.urls import path,include, re_path
from django.contrib import admin
from APP.views import mostrar_inicio, api,PanelLogin, PanelLogout,ClientesDeleteView, nosotros, lista_clientes , delete, ClienteUpdate, filtro,UserDetalle,UserUpdate,cambiar_contraseña,UserLogout,filtroanual,getapi
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', mostrar_inicio, name='raiz'),
    path('api/', api, name='api'),
    path("nosotros", nosotros, name="nosotros"),
    path("login/", PanelLogin.as_view(), name="login"),
    path("logout/", PanelLogout.as_view(), name="logout"),
    # path('clientes/create/', ClientesCreateView.as_view(), name ="clientess" ),
    path("clientes/" ,lista_clientes, name="clientes"),
    # path("delete/<id>" , delete, name="eliminar"),
    path("clientes/<pk>/delete" ,ClientesDeleteView.as_view(),name="eliminar"),
    path('admin/', admin.site.urls),
    path(r'^editar/(?P<pk>\d+)$', ClienteUpdate.as_view(), name="editar"),
    path('filtro/', filtro, name='filtro'),
    path("userUpdate/<pk>/" , UserDetalle.as_view(), name="userUpdate"),
    path("actualizacion/<pk>/edit", UserUpdate.as_view(), name="editarusuario"),
    path("logout/", UserLogout.as_view(), name="logout"),
    path("cambiarPass/", cambiar_contraseña, name="cambiarPass" ),
    path("getapi/<id>/", getapi, name="getapi" ),
    path("filtroanual/", filtroanual, name="filtroanual" ),

    #RECUPERACION DE CONTRASEÑA
    path("reset_password/" ,auth_views.PasswordResetView.as_view(template_name="APP/password_reset.html", html_email_template_name='APP/password_reset_email.html'), name="password_reset" ),
    path("reset_password_send/", auth_views.PasswordResetDoneView.as_view(template_name="APP/password_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(template_name="APP/password_confirm.html"), name='password_reset_confirm'),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="APP/password_complete.html"), name='password_reset_complete'),



]
