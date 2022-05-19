from jsonfile import JsonFile


class Cliente(JsonFile):
    def __init__(self, nombre='',rfc='',direccion=''):
        super(Cliente,self).__init__('clientes.json')
        self.nombre=nombre
        self.rfc=rfc
        self.direccion=direccion
        self.__idx__=0
        self.filename='clientes.json'
    
    def add(self, cliente):
        self.lista.append(cliente)

    def eliminar(self,cliente):
        self.lista.remove(cliente)

    def getCliente(self,index):
        return self.lista[index]

    def modificar(self,index,cliente):
        self.lista[index]=cliente

    def tamano(self):
        return len(self.lista)
    
    def getlist(self):
        return self.lista

    def __str__(self):
        return self.nombre+ ' \t\t'+self.rfc+ ' \t\t'+ self.direccion

    def toObjects(self):
        lista=list()
        data=self.getDataJson()
        for x in data:
            lista.append(Cliente(nombre=x['nombre'],rfc=x['rfc'],direccion=x["direccion"]))
        self.lista=lista

    def getDictory(self):
        return {
            "nombre":self.nombre,
			"codigo":self.rfc,
			"precio":self.direccion
		}

    def listDict(self):
        listDiccionario=list()
        for x in self.lista:
            listDiccionario.append(x.__dict__)
            print(x.getDictory())
            return listDiccionario

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