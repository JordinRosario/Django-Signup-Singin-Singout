from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('usuario/crear',views.crear_usuario, name='crearusuario'),
    path('usuario/sesion/cerrar', views.cerrar_sesion, name='cerrarsesion'),
    path('usuario//sesion/iniciar', views.iniciar_sesion, name='iniciarsesion'),
]
