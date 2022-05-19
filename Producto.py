from jsonfile import JsonFile
import json
class Producto(JsonFile): 

	def __init__(self,nombre='',codigo='',precio=''):
		super(Producto, self).__init__('productos.json')
		self.nombre=nombre
		self.codigo=codigo
		self.precio=precio
		self.__idx__ = 0
		self.filename="productos.json"


	def add(self, producto):
		self.lista.append(producto)

	def eliminar(self,producto):
		self.lista.remove(producto)

	'''
	#con index eliminar elemento
	def eliminar(self,idx):
		del self.lista[index]
	'''

	def getProducto(self,index):
		return self.lista[index]

	def modificar(self,index,producto):
		self.lista[index]=producto

	def tamano(self):
		return len(self.lista)

	def getlist(self):
		return self.lista
		
	def __str__(self):
		return self.nombre+ ' \t\t'+self.codigo+ ' \t\t'+ str(self.precio)

	def toObjects(self):
		lista=list()
		data=self.getDataJson()
		for x in data:
				lista.append(Producto(nombre=x['nombre'],codigo=x['codigo'],precio=x["precio"]))
		self.lista=lista


	def getDictory(self):
		return {
			"nombre":self.nombre,
			"codigo":self.codigo,
			"precio":self.precio
		}
	def listDict(self):
		listDiccionario=list()
		for x in self.lista:
			listDiccionario.append(x.__dict__)
			print(x.getDictory())
		return listDiccionario;

	def __iter__(self):
		self.__idx__ = 0
		return self
	def __next__(self):
		if self.__idx__<len(self.lista):
			x =self.lista[self.__idx__]
			self.__idx__+=1 
			return x
		else:
			raise StopIteration 