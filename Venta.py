from msilib.schema import SelfReg
from Cliente import Cliente


class Venta(Cliente):
    def __init__(self, nombre='', rfc='', direccion='',fecha='', subtotal=0, iva=0,total=0 ,dvLista=list()):
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion
        self.fecha=fecha
        self.subtotal = subtotal
        self.iva = iva
        self.total = total
        self.dvLista = dvLista
        self.filename = 'ventas.json'

    def __iva__(self):
        self.iva=self.subtotal*0.16

    def __subtotal__(self):
        for i in self.dvLista:
            self.subtotal+=i.total

    def __total__(self):
        self.total=self.subtotal+self.iva

    def calcular(self):
        self.__subtotal__()
        self.__iva__()
        self.__total__()