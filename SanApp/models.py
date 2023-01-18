from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.IntegerField()
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, tel:{self.celular}, Dirección: {self.direccion} - {self.localidad}"

class Pedido(models.Model):
    cliente = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    def __str__(self):
        return f"Pedido: {self.cantidad} {self.producto} para {self.cliente}"
    
class Cambios(models.Model):
    cliente = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    motivo = models.CharField(max_length=200)
    def __str__(self):
        return f"Cambios: {self.cantidad} {self.producto} debido a {self.motivo} para {self.cliente}"
