from Cliente import Cliente
from pymongo import MongoClient
import pymongo
import json

class MongoBD:

    def get_database(self,collection):
        # Provide the mongodb atlas url to connect python to mongodb using pymongo
        CONNECTION_STRING = 'mongodb+srv://admin:admin123@sandbox.swi5m.mongodb.net/SystemVentas?retryWrites=true&w=majority'

        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        from pymongo import MongoClient
        client = MongoClient(CONNECTION_STRING)

        # Create the database for our example (we will use the same database throughout tjt3dhe tutorial
        dbname = client['SystemVentas']
        collection_name = dbname[collection]

        return collection_name

    def inserJSON(self):
        # Get the database
        dbname = self.get_database()
        # Create a new collection
        collection_name = dbname["Productos"]

        with open('productos.json') as file: 
            file_data = json.load(file) 
        
            if isinstance(file_data, list): 
                collection_name.insert_many(file_data)   
            else: 
                collection_name.insert_one(file_data) 
    
    def obtener(self):
        dbcollection = self.get_database()
        return dbcollection.find()

    def InsertarCliente(self,clientes):
        collection="Cliente"
        dbcollection = self.get_database(collection)
        dbcollection.insert_one({"nombre": clientes.nombre,"rfc": clientes.rfc,"direccion": clientes.direccion})
        return 'Cliente Agregado a DB'

    def ActualizarCliente(self, rfc,cliente):
        collection="Cliente"
        dbcollection = self.get_database(collection)
        resultado = dbcollection.update_one(
            {
            'rfc': rfc
            }, 
            {
                '$set': {
                    "nombre": cliente.nombre,
                    "rfc": cliente.rfc,
                    "direccion": cliente.direccion,
                }
            })
        return resultado.modified_count

    def EliminarCliente(self,rfc):
        collection="Cliente"
        dbcollection = self.get_database(collection)
        resultado = dbcollection.delete_one(
            {
            'rfc': rfc
            })
        return resultado.deleted_count

    def InsertarProdcuto(self,productos):
        collection="Productos"
        dbcollection = self.get_database(collection)
        dbcollection.insert_one({"nombre": productos.nombre,"codigo": productos.codigo,"precio": productos.precio})

    def ActualizarProducto(self, codigo,producto):
        collection="Productos"
        dbcollection = self.get_database(collection)
        resultado = dbcollection.update_one(
            {
            'codigo': codigo
            }, 
            {
                '$set': {
                    "nombre": producto.nombre,
                    "codigo": producto.codigo,
                    "precio": producto.precio,
                }
            })
        return resultado.modified_count

    def EliminarProducto(self,codigo):
        collection="Productos"
        dbcollection = self.get_database(collection)
        resultado = dbcollection.delete_one(
            {
            'codigo': codigo
            })
        return resultado.deleted_count

    def CarritoVenta(self,listaCarrito):
        self.listadict=[]
        for b in listaCarrito:
            self.listadict.append(b.__dict__)
        return self.listadict

    def InsertarVenta(self,venta):
        collection="Ventas"
        dbcollection = self.get_database(collection)
        listaproductos=self.CarritoVenta(venta.dvLista)
        dbcollection.insert_one({"nombre": venta.nombre,"rfc": venta.rfc,"direccion": venta.direccion,"productos":listaproductos,"subtotal":venta.subtotal,"iva":venta.iva,"total":venta.total})

    def MostrarVentas(self):
        collection="Ventas"
        dbcollection = self.get_database(collection)
        return dbcollection.find()


# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    mbd=MongoBD()
    menu = """Bienvenido a la tienda.
    1 - Insertar producto
    2 - Ver todos
    3 - Actualizar
    4 - Eliminar
    5 - Salir
    """
    eleccion = None
    while (eleccion != 5):
        print(menu)
        eleccion = int(input("Elige: "))
        if eleccion == 1:
            print("Insertar")
            nombre = input("Nombre del Cliente: ")
            precio = input("RFC del Cliente: ")
            cantidad = input("Direccion del Cliente: ")
            Ncliente = Cliente(nombre, precio, cantidad)
            id = mbd.insertar(Ncliente)
            print(id)


        
        
        
    