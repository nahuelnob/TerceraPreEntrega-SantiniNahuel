from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    celular = forms.IntegerField()
    direccion = forms.CharField(max_length=50)
    localidad = forms.CharField(max_length=50)
    
class PedidosFormulario(forms.Form):
    cliente = forms.CharField(max_length=50)
    producto = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    
class CambiosFormulario(forms.Form):
    cliente = forms.CharField(max_length=50)
    producto = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    motivo = forms.CharField(max_length=500)