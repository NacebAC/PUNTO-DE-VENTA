from ProductoVenta import ProductoVenta
from MongoDB import MongoBD
from Producto import Producto
import copy
import json 
import os

class InterfaceProducto():
	"""docstring for interfaceProducto"""
	def __init__(self): 
		self.lista=Producto()
		self.lista.toObjects()
		print(self.lista)
	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')

	def cantidadProducto(self,p):
		p.cantidad=float(input("Cantidad de Producto:"))
		p.calcular()
		return p

	def nuevoProducto(self):
		p=Producto()
		mbd=MongoBD()
		p.nombre=input("Nombre del Producto:")
		p.codigo=input("Codigo del Producto:")
		p.precio=float(input("Precio del Producto:"))
		mbd.InsertarProdcuto(p)
		return p 

	def mostrarProducto(self,lista=None):
		self.cls()
		print("\n\n"+"*"*30+"Datos de Productos"+"*"*30)
		if(lista==None):
			mylista=self.lista
		else:
			mylista=lista
		print("ID".ljust(5)+"\t\t"+'Nombre'.ljust(20)+'\t\t'+'Codigo'.ljust(20)+'\t\tPrecio')
		print(mylista)
		i=0
		for p in mylista:
			print(str(i).ljust(5)+"\t\t"+str(p))
			i+=1
		input("oprime enter para continuar .....")

	def buscarProducto(self,code):
		mylista=[p for p in self.lista if p.codigo == code]
		self.mostrarProducto(mylista)

	def getListaProductos(self):
		return self.lista

	def modificarProducto(self):
		mbd=MongoBD()
		id=int(input("Introduce ID:"))
		p=self.lista.getlist()[id]
		codigo=p.codigo
		cadena=input("Nombre del Producto:")
		if(len(cadena)>0):
			p.nombre=cadena
		cadena=input("Codigo del Producto:")
		if(len(cadena)>0):
			p.codigo=cadena
		cadena=input("Precio del Producto:")
		if(len(cadena)>0):
			p.precio=float(cadena)
		mbd.ActualizarProducto(codigo,p)
		self.lista.modificar(id,p)
    
	def eliminarProducto(self):
		mbd=MongoBD()
		id=input("Introduce ID:")
		id=int(id)
		codigo=self.lista.getProducto(id)
		mbd.EliminarProducto(codigo.codigo)
		self.lista.eliminar(self.lista.getProducto(id))

	def menuProductos(self):
		a=10;
		while a!=0:
			print("\n\n"+"*"*30+"Menu de Productos"+"*"*30)
			print("1) Nuevo Producto")
			print("2) Modificar Producto")
			print("3) Eliminar Producto")
			print("4) Consultar Producto")
			print("5) Mostrar Producto")
			print("0) Salir")
			a=input("Selecciona una opción: ")
			if(a=='1'):
				p=self.nuevoProducto()
				self.lista.add(p)
				self.lista.toJson(self.lista)
			elif(a=='2'):
				self.mostrarProducto()
				self.modificarProducto()
				self.lista.toJson(self.lista)
			elif(a=='3'):
				self.mostrarProducto()
				self.eliminarProducto()
				self.lista.toJson(self.lista)
			elif(a=='4'):
				codigo=input("dame el codigo:")
				self.buscarProducto(codigo)
			elif(a=='5'):
				self.mostrarProducto()
			elif(a=='0'):
				break;
			else:
				print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
				input()

if __name__=='__main__':
	ip=InterfaceProducto()
	ip.menuProductos()