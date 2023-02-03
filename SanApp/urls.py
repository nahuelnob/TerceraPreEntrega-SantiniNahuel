from django.urls import path
from SanApp.views import *

#CAMBIAR LOS GUIONES BAJOS DE LAS URLS

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('nuevoCliente/', cliente, name="Nuevo_cliente"),
    path('comprar/', comprar, name="Comprar"),
    path('cambios/', cambiar, name="Cambiar"),    
    path('finCompra/', finCompra, name="FinCompra"),
    path('que_hacer/', que_hacer, name="Que_hacer"),
    path('hacerPedidos/', hacer_pedidos, name="Hacer_pedido"),
    path('hacerCambios/', hacer_cambios, name="Hacer_cambios"),
    path('buscarCliente/', buscar_cliente, name="Buscar_cliente"),
    path('leerCliente/', leer_cliente, name="Leer_cliente"),
    path('crear_cliente/', crear_cliente, name="Crear_cliente"),
    path('profe_cliente_nuevo', profe_cliente_nuevo, name="profe_cliente_nuevo"),
    path('detalle_cliente/<int:id>/', detalle_cliente, name="detalle_cliente"),
    path('editar_cliente/<int:id>/', editar_cliente, name="editar_cliente"),
    path('eliminar_cliente/<int:id>/', eliminar_cliente, name="eliminar_cliente"), 
    path('leer_pedidos', PedidosListView.as_view(), name="leer_pedidos"),
    path('crear_pedidos', PedidosCreateViews.as_view(), name="crear_pedido"),
    path('editar_pedido/<int:pk>/', PedidosUpdateViews.as_view(), name="editar_pedido"),
    path('borrar_pedido/<int:pk>/', PedidosDeleteViews.as_view(), name="borrar_pedido"),
    path('detalle_pedido/<int:pk>/', PedidosDetailViews.as_view(), name="detalle_pedido"),
    path('registro/', registro, name='registro'),
    path('login/', login_views, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('editar_perfil/', ProfileUpdateView.as_view(), name='editar_perfil'),
    path('la_empresa/', la_empresa, name="la_empresa"),
    path('leer_comentarios', ComentarioLw.as_view(), name="leer_comentarios"),
    path('crear_comentario', crear_comentario, name="crear_comentario"),
    path('detalle_comentario/<int:pk>/', ComentarioDeV.as_view(), name='detalle_comentario'),
    
]