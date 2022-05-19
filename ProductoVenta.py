from Producto import Producto
import copy

class ProductoVenta(Producto):
	def __init__(self, nombre='', codigo='', precio='', cantidad=0, subtotal=0, iva=0,total=0, lista=list()):
		self.nombre = nombre
		self.codigo = codigo
		self.precio = precio
		self.cantidad = cantidad
		self.subtotal = subtotal
		self.iva = iva
		self.total = total
		self.lista = lista
		
	def __str__(self):
		if(self.cantidad>0):
			return (self.nombre).ljust(20)+ ' \t\t'+(self.codigo).ljust(20)+ ' \t\t'+str(self.precio).ljust(20)+ ' \t\t'+str(self.cantidad).ljust(20)+ ' \t\t'+str(self.subtotal).ljust(20)+ ' \t\t'+str(self.iva).ljust(20)+ ' \t\t'+str(self.total).ljust(20)
		else:
			return (self.nombre).ljust(20)+ ' \t\t'+(self.codigo).ljust(20)+ ' \t\t'+str(self.precio).ljust(20)

	def __iva__(self):
		self.iva=self.cantidad*self.precio*0.16

	def __subtotal__(self):
		self.subtotal=self.cantidad*self.precio

	def __total__(self):
		self.total=self.subtotal+self.iva

	def calcular(self):
		self.__iva__();
		self.__subtotal__();
		self.__total__();

if __name__=='__main__':
	producto=ProductoVenta('Laptop','L1',0.0)
	producto.nombre='Laptop'
	producto.codigo='L1'
	producto.precio=5400.0
	producto.calcular()

	producto1=ProductoVenta('Laptop','L2',0.0)
	producto1.nombre='Laptop'
	producto1.codigo='L2'
	producto1.precio=7400.0
	producto1.calcular()

	print(producto)
	lista=ProductoVenta()
	lista.add(producto)
	lista.add(producto1)
	print("Tamano:",lista.tamano())
	# copiar objeto 
	productocopy = copy.copy(producto)
	productocopy.cantidad=10

	lista.add(productocopy)

	# import copy
	print("Vista:")
	for x in lista.getlist():
		print("Objeto:",x)