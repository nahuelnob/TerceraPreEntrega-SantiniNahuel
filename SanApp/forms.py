from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
import email


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

class ComentariosFormulario(forms.Form):
    usuario = forms.CharField(max_length=50)
    comentario = forms.CharField(max_length=248)
 
 
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        

    