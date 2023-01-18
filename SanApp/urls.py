from django.urls import path
from SanApp import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('nuevoCliente/', views.cliente, name="Nuevo_cliente"),
    path('comprar/', views.comprar, name="Comprar"),
    path('cambios/', views.cambiar, name="Cambiar"),    
    path('finCompra/', views.finCompra, name="FinCompra"),
    path('que_hacer/', views.que_hacer, name="Que_hacer"),
    path('hacerPedidos/', views.hacer_pedidos, name="Hacer_pedido"),
    path('hacerCambios/', views.hacer_cambios, name="Hacer_cambios"),
    path('buscarCliente/', views.buscar_clientes, name="Buscar_cliente")
]