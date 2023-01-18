from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from SanApp.models import *
from SanApp.forms import *


def inicio(request):
    return render(request, "SanApp/inicio.html")

def comprar(request):
    return render(request, "SanApp/comprar.html")

def cambiar(request):
    return render(request, "SanApp/cambiar.html")

def finCompra(request):
    return render(request, "SanApp/finCompra.html")

def que_hacer(request):
    return render(request, "SanApp/que_hacer.html")

def buscar_clientes(request):
    cliente = Cliente.objects.all()
    contexto = {"cliente":cliente}
    return render(request, "SanApp/buscar_cliente.html", contexto)
    
def cliente(request):
    if request.method == "POST":
        mi_formu = ClienteFormulario(request.POST)
        print(mi_formu)
        
        if mi_formu.is_valid:
            informacion = mi_formu.cleaned_data
            cliente = Cliente(nombre=informacion["nombre"], apellido=informacion["apellido"], celular=informacion["celular"], direccion=informacion["direccion"], localidad=informacion["localidad"])
            cliente.save()
            return render(request, "SanApp/que_hacer.html")
    
    else:
        mi_formu = ClienteFormulario()
    
    return render(request,"SanApp/nuevo_cliente.html", {"mi_formu":mi_formu})



def hacer_pedidos(request):
    if request.method == "POST":
        mi_formu = PedidosFormulario(request.POST)
        print(mi_formu)
        
        if mi_formu.is_valid:
            informacion = mi_formu.cleaned_data
            pedidos = Pedido(producto=informacion["producto"], cantidad=informacion["cantidad"], cliente=informacion["cliente"])
            pedidos.save()
            return render(request, "SanApp/finCompra.html")
    
    else:
        mi_formu = PedidosFormulario()
    
    return render(request, "SanApp/hacer_pedido.html", {"mi_formu":mi_formu})



def hacer_cambios(request):
    if request.method == "POST":
        mi_formu = CambiosFormulario(request.POST)
        print(mi_formu)
        
        if mi_formu.is_valid:
            informacion = mi_formu.cleaned_data
            cambios = Cambios(producto=informacion["producto"], cantidad=informacion["cantidad"], motivo=informacion["motivo"], cliente=informacion["cliente"])
            cambios.save()
            return render(request, "SanApp/finCompra.html")
    
    else:
        mi_formu = CambiosFormulario()
    
    return render(request, "SanApp/hacer_cambios.html", {"mi_formu":mi_formu})
