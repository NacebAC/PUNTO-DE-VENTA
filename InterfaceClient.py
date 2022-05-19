from Cliente import Cliente
from MongoDB import MongoBD
import copy
import json 
import os


class InterfaceCliente():
	"""docstring for interfaceProducto"""
	def __init__(self): 
		self.lista=Cliente(); 
		self.lista.toObjects();

	def cls(self):
		os.system('cls' if os.name=='nt' else 'clear')

	def nuevoCliente(self):
		c=Cliente()
		mbd=MongoBD()
		c.nombre=input("Nombre del Cliente:")
		c.rfc=input("RFC del Cliente:")
		c.direccion=input("Direccion del Cliente:")
		mbd.InsertarCliente(c)
		return c 

	def mostrarCliente(self,lista=None):
		self.cls()
		print("\n\n"+"*"*30+"Datos de Clientes"+"*"*30)
		if(lista==None):
			mylista=self.lista
		else:
			mylista=lista
		print("ID".ljust(5)+"\t\t"+'Nombre'.ljust(20)+'\t\t'+'RFC'.ljust(20)+'\t\tDireccion')
		i=0
		for c in mylista:
			print(str(i).ljust(5)+"\t\t"+str(c))
			i+=1
		input("oprime enter para continuar .....")

	def buscarCliente(self,code):
		mylista=[c for c in self.lista if c.rfc == code]
		self.mostrarCliente(mylista)

	def getListaClientes(self):
		return self.lista

	def modificarCliente(self):
		mbd=MongoBD()
		id=int(input("Introduce ID:"))
		c=self.lista.getlist()[id]
		rfc=c.rfc
		cadena=input("Nombre del Cliente:")
		if(len(cadena)>0):
			c.nombre=cadena
		cadena=input("RFC del Cliente:")
		if(len(cadena)>0):
			c.rfc=cadena
		cadena=input("Direccion del Cliente:")
		if(len(cadena)>0):
			c.direccion=cadena
		mbd.ActualizarCliente(rfc,c)
		self.lista.modificar(id,c)
    
	def eliminarCliente(self):
		mbd=MongoBD()
		id=input("Introduce ID:")
		id=int(id)
		rfc=self.lista.getCliente(id)
		mbd.EliminarCliente(rfc.rfc)
		self.lista.eliminar(self.lista.getCliente(id))

	def menuCliente(self):
		a=10;
		while a!=0:
			self.cls()
			print("\n\n"+"*"*30+"Menu de Clientes"+"*"*30)
			print("1) Nuevo Cliente")
			print("2) Modificar Cliente")
			print("3) Eliminar Cliente")
			print("4) Consultar Cliente")
			print("5) Mostrar Cliente")
			print("0) Salir")
			a=input("Selecciona una opción: ")
			if(a=='1'):
				p=self.nuevoCliente()
				self.lista.add(p)
				self.lista.toJson(self.lista)
			elif(a=='2'):
				self.mostrarCliente()
				self.modificarCliente()
				self.lista.toJson(self.lista)
			elif(a=='3'):
				self.mostrarCliente()
				self.eliminarCliente()
				self.lista.toJson(self.lista)
			elif(a=='4'):
				codigo=input("Ingrese el RFC:")
				self.buscarCliente(codigo)
			elif(a=='5'):
				self.mostrarCliente()
			elif(a=='0'):
				break;
			else:
				print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
				input()

if __name__=='__main__':
	ip=InterfaceCliente()
	ip.menuCliente()