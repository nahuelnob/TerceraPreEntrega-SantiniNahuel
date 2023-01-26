from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from SanApp.models import *
from SanApp.forms import *
from SanApp.forms import UserRegisterForm



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

def buscar_cliente(request):
    if request.method == "POST":
        data = request.POST
        cliente = Cliente.objects.filter(nombre__contains=data['nombre'])
        contexto = {'cliente': cliente}
        
        return render (request, 'SanApp/leer_cliente.html', contexto)
    else:
        return render(request, "SanApp/buscar_cliente.html",)
    
def leer_cliente(request):
    cliente = Cliente.objects.all()
    contexto = {"cliente":cliente}
    
    return render(request, "SanApp/leer_cliente.html", contexto)
    


def crear_cliente(request):
    """
    creado a mano
    
    """
    if request.method == "POST":
        data = request.POST
        cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], celular=data['celular'], direccion=data["direccion"], localidad=data["localidad"])
        cliente.save()
        return redirect (reverse("Leer_cliente"))
    else: #Seria un GET
        return render (request, "SanApp/formulario_cliente.html")
    
def profe_cliente_nuevo(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], celular=data['celular'], direccion=data["direccion"], localidad=data["localidad"])
            cliente.save()
            return redirect (reverse("Leer_cliente"))
    else: #Seria un GET
        formulario = ClienteFormulario()
        contexto = {'formulario':formulario}
        return render (request, "SanApp/profe_cliente_nuevo.html", contexto)
    
def detalle_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    contexto = {"cliente":cliente}
    return render(request, "SanApp/detalle_cliente.html", contexto)

def editar_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    
    if request.method == "POST":
        mi_formu = ClienteFormulario(request.POST)
        print(mi_formu)
        
        if mi_formu.is_valid():
            info = mi_formu.cleaned_data
            cliente.nombre = info['nombre']
            cliente.apellido = info['apellido']
            cliente.celular = info['celular']
            cliente.direccion = info['direccion']
            cliente.localidad = info['localidad']
            cliente.save()
            return render(request, "SanApp/que_hacer.html")
    
    else:
        inicial = {'nombre':cliente.nombre, 'apellido':cliente.apellido, 'celular':cliente.celular, 'direccion':cliente.direccion, 'localidad':cliente.localidad}
        mi_formu = ClienteFormulario(initial=inicial)
    
    return render(request,"SanApp/nuevo_cliente.html", {"mi_formu":mi_formu,"id":id})
        
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        cliente.delete() 
        return redirect (reverse("Leer_cliente")) 
    

class PedidosListView(ListView):
    model = Pedido
    template_name = "SanApp/leer_pedidos.html"
    
class PedidosCreateViews(CreateView):
    model = Pedido
    url_exitosa = "SanApp/hacer_pedido.html"
    fields = ['cliente', 'producto', 'cantidad']
    
class PedidosUpdateViews(UpdateView):
    model = Pedido
    success_url = "/SanApp/leer_pedidos"
    fields = ['cliente', 'producto', 'cantidad']
    
class PedidosDeleteViews(DeleteView):
    model = Pedido
    success_url = reverse_lazy('leer_pedidos')
    template_name = 'SanApp/confirmar_eliminacion_pedido.html'

class PedidosDetailViews(DetailView):
    model = Pedido
    susuccess_url = "/SanApp/detalle_pedido"
    template_name = "SanApp/detalle_pedido.html"
    
def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect (reverse("Inicio"))
    else:
        formulario = UserRegisterForm()
        contexto = {'form': formulario}
        return render (request, "SanApp/registro.html", contexto)
        