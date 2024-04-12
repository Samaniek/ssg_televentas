from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.clientes_view, name='clientes_view'),
    #path('agregar_notas/', views.agregar_notas, name='agregar_notas'),
    #path('cliente/<str:cliente_cedula>/', views.clientes_view, name='cliente_view'),
    #path('cliente/', views.guardar_cliente, name='guardar_cliente'),  # Nueva ruta para manejar el guardado del cliente
    #path('cliente/', views.clientes_view, name='cliente'),
    #path('clientes/', views.clientes_view, name='clientes'),
    # Aquí agregar otras URLs según sea necesario
]
