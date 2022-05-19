import os.path
import json 

class JsonFile: 
	def __init__(self,filename):
		self.filename=filename

	def getDataJson(self):		
		data=[]
		if(os.path.isfile(self.filename)):
			file = open(self.filename, "r")
			data=json.loads(file.read())
		return data 

	def toJson(self,listaProductos):		
		file = open(self.filename, "w")
		file = json.dump([ob.__dict__ for ob in listaProductos], file,indent=4)

	def VtoJson(self, listaVenta):
		file = open(self.filename, "w")
		file = json.dump([ob.__dict__ for ob in listaVenta], file,indent=4)

