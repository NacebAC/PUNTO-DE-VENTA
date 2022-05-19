from audioop import add
from inspect import _void
import json
from wsgiref.util import request_uri
from InterfaceProduct import InterfaceProducto
from MongoDB import MongoBD
from Producto import Producto
from ProductoVenta import ProductoVenta
from Cliente import Cliente
from Venta import Venta
from datetime import datetime
from Reporte import Reporte

class InterfaceVentas():
    def __init__(self):
        self.lv=[]
        self.listaReporte=[]
        self.lvD=[]
        self.AddJson()
        self.lp = Producto()
        self.lp.toObjects()
        self.lc=Cliente()
        self.lc.toObjects()

    def addReporte(self):
        i=0
        subtotal=0
        fechas=[]
        fechas.append(self.lv[i].fecha)
        print (self.lv[i].fecha)
        for a in range(len(self.lv)):
            i+=1
            fechas.append(self.lv[a].fecha)
            if(fechas[i]!=fechas[i-1]):
                print (self.lv[a].fecha)
        fecha=input("Fecha: ")
        for a in self.lv:
            if(fecha==a.fecha):
                subtotal+=a.total
                iva=subtotal*0.16
                total=iva+subtotal
                report=Reporte(self.lv,subtotal,iva,total)
                self.listaReporte.append(report)
        self.mostrarReporte(report)

    def mostrarReporte(self,report):
        print("**"*10)
        print("Subtotal:" + str(report.subtotal))
        print("IVA:" + str(report.iva))
        print("TOTAL:" + str(report.total))

    def detalleReporte(self):
        i=0
        subtotal=0
        iva=0
        total=0
        fechas=[]
        fechas.append(self.lv[i].fecha)
        print (self.lv[i].fecha)
        for a in range(len(self.lv)):
            i+=1
            fechas.append(self.lv[a].fecha)
            if(fechas[i]!=fechas[i-1]):
                print (self.lv[a].fecha)
        fecha=input("Fecha: ")
        for a in self.lv:
            if(fecha==a.fecha):
                subtotal+=a.subtotal
                iva+=a.iva
                total+=a.total
                report=Reporte(self.lv,subtotal,iva,total)
                print("**"*20)
                print("Fecha: " + a.fecha)
                print("Cliente: " + a.nombre)
                print("*"*20+"PRODUCTOS"+"*"*20)
                print("Producto"+"\t\t"+"Subtotal"+"\t\t"+"IVA"+"\t\t"+"Total")
                for b in a.dvLista:
                    print(str(b.nombre)+"\t\t"+str(b.subtotal)+"\t\t"+str(b.iva)+"\t\t"+str(b.total))
                print("Subtotal: " + str(a.subtotal))
                print("IVA: " + str(a.iva))
                print("Total: " + str(a.total))
        self.mostrarReporte(report)



    def AddJson(self):
        f=open("ventas.json","r")
        aux= f.read()
        self.lvD=json.loads(aux)
        f.close()
        self.VtoObject()

    def VtoObject(self):
        for venta in self.lvD:
            listanueva=[]
            for producto in venta["dvLista"]:
                nuevoProducto=ProductoVenta(producto["nombre"],producto["codigo"],producto["precio"],producto["cantidad"],producto["subtotal"],producto["iva"],producto["total"],producto["lista"])
                listanueva.append(nuevoProducto)
            nuevaVenta=Venta(venta["nombre"],venta["rfc"],venta["direccion"],venta["fecha"],venta["subtotal"],venta["iva"],venta["total"],listanueva)
            self.lv.append(nuevaVenta)

    def VtoJson(self):
        self.lvD=[]
        if self.lv!=[]:
            for venta in self.lv:
                nuevalist=[]
                aux=venta.__dict__
                for j in venta.dvLista:
                    nuevalist.append(j.__dict__)
                aux["dvLista"]=nuevalist
                self.lvD.append(aux)
            f=open("ventas.json","w")
            aux=json.dumps(self.lvD,indent=4)
            f.write(aux)
            f.close
        else:
            pass

    def addVenta(self):
        mdb=MongoBD()
        self.mostrarCliente()
        idc=int(input("Escribe ID del Cliente: "))
        c=self.lc.getCliente(idc)
        proVent=self.AgregarProductosVenta()
        v=Venta()
        v.nombre=c.nombre
        v.rfc=c.rfc
        v.direccion=c.direccion
        v.fecha=datetime.today().strftime('%Y-%m-%d')
        v.dvLista=proVent
        v.calcular()
        
        mdb.InsertarVenta(v)
        return v

    def AgregarProductosVenta(self):
        self.dvLista=[]
        seguir='S'
        while(seguir=='S'):
            self.VerProductos()
            id=int(input("Escribe ID del Producto: "))
            p = self.lp.getlist()[id]
            v = ProductoVenta()
            v.nombre = p.nombre
            v.codigo = p.codigo
            v.precio = p.precio
            v.cantidad = int(input("Cantidad de Producto:"))
            v.calcular()
            self.dvLista.append(v)
            print('¿Desea agregar otro producto?(S/N)')
            seguir=input('OPCION: ')
        return self.dvLista

    def mostrarCliente(self,lista=None):
        print("\n\n"+"*"*30+"Datos de Clientes"+"*"*30)
        if(lista==None):
            mylista=self.lc
        else:
            mylista=lista
        print("ID".ljust(5)+"\t\t"+'Nombre'.ljust(20)+'\t\t'+'RFC'.ljust(20)+'\t\tDireccion')
        i=0
        for c in mylista:
            print(str(i).ljust(5)+"\t\t"+str(c))
            i+=1
        input("oprime enter para continuar .....")

    def VerProductos(self, lista=None):
        print("\n" + "*" * 30 + "Datos de Productos" + "*" * 30)
        if (lista == None):
            mylista = self.lp
        else:
            mylista = lista
        print("ID".ljust(5) + "\t\t" + 'Nombre'.ljust(10) + '\t\t' + 'Codigo'.ljust(10) + '\t\t'+'Precio'.ljust(10)+
              '\t\t'+'Cantidad'.ljust(10)+ '\t\t'+'Subtotal'.ljust(10)+ '\t\t'+'IVA'.ljust(10)+ '\t\t'+'Total'.ljust(10))
        i = 0
        for p in mylista:
            print(str(i).ljust(5) + "\t\t" + str(p.nombre))
            i += 1

    def VerVentas(self, lista=None):
        if (lista == None):
            mylista = self.lv
        else:
            mylista = lista
        for a in mylista:
            print("NOMBRE: " + a.nombre)
            print("\n" + "*" * 30 + "Datos de Ventas" + "*" * 30)
            print("ID" + "\t\t" + 'Producto' +'\t\t' + 'Precio'+ '\t\t'+'Cantidad'+ '\t\t' + 'Subtotal'+ '\t\t' + 'IVA'+ '\t\t' + 'Total')
            i = 0
            for p in a.dvLista:
                print(str(i)+'\t\t'+str(p.nombre)+'\t\t'+str(p.precio)+'\t\t'+str(p.cantidad)+'\t\t'+str(p.subtotal)+'\t\t'+str(p.iva)+'\t\t'+str(p.total))
                i += 1
            print("SUBTOTAL: " + str(a.subtotal))
            print("IVA: " + str(a.iva))
            print("TOTAL: " + str(a.total))

    def buscarVenta(self):
        index=int(input("Escribe ID de la Venta: "))
        for a in range(len(self.lv)):
            if index ==a:
                print("NOMBRE: " + str(self.lv[index].nombre))
                print("\n" + "*" * 30 + "Datos de Ventas" + "*" * 30)
                print("ID" + "\t\t" + 'Producto' +'\t\t' + 'Precio'+ '\t\t'+'Cantidad'+ '\t\t' + 'Subtotal'+ '\t\t' + 'IVA'+ '\t\t' + 'Total')
                i = 0
                for p in self.lv[index].dvLista:
                    print(str(i)+'\t\t'+str(p.nombre)+'\t\t'+str(p.precio)+'\t\t'+str(p.cantidad)+'\t\t'+str(p.subtotal)+'\t\t'+str(p.iva)+'\t\t'+str(p.total))
                    i += 1
                print("SUBTOTAL: " + str(self.lv[index].subtotal))
                print("IVA: " + str(self.lv[index].iva))
                print("TOTAL: " + str(self.lv[index].total))

    def eliminarVenta(self):
        index=int(input("Escribe ID de la Venta: "))
        for a in range(len(self.lv)):
            if index ==a:
                self.lv.pop(index)
                print ('Venta Eliminada')

    def menuVentas(self):
        a = 10
        while a != 0:
            print("\n" + "*" * 30 + "Menu de Productos" + "*" * 30)
            print("1) Realizar Venta")
            print("2) Ver Ventas")
            print("3) Eliminar Venta")
            print("4) Mostrar Venta")
            print("5) Ver Reporte")
            print("6) Detalle Reporte")
            print("x) Salir")
            a = input("Selecciona una opción: ")
            if (a == '1'):
                p = self.addVenta()
                self.lv.append(p)
                self.VtoJson()
                print ('>>>>>>>>>>> Venta Agregada')
            elif (a == '2'):
                self.VerVentas()
            elif (a == '3'):
                self.eliminarVenta()
            elif (a == '4'):
                self.buscarVenta()
            elif (a == '5'):
                report=self.addReporte()
            elif (a == '6'):
                report=self.detalleReporte()
            elif (a == 'x'):
                break
            else:
                print("Opcion invalida")