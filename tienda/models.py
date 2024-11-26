from django.db import models

class Componente(models.Model):
	nombre = models.CharField(max_length=100)
	tipo = models.ForeignKey('TipoComponente', on_delete=models.CASCADE)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='componentes/', null=True, blank=True)
	precio = models.IntegerField()
	stock = models.IntegerField()

	def __str__(self):
		return self.nombre
	
class TipoComponente(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre
	
class Venta(models.Model):
	usuario = models.CharField(max_length=100, null=True)
	total = models.IntegerField()

	def __str__(self):
		return str(self.id)

class DetalleVenta(models.Model):
	componente = models.ForeignKey('Componente', on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	subtotal = models.IntegerField()
	venta = models.ForeignKey('Venta', on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)