from InterfaceClient import InterfaceCliente
from InterfaceProduct import InterfaceProducto
from InterfaceVenta import InterfaceVentas

def menu():
    a=10
    while a!=0:
        print("\n\n"+"*"*30+" MENU "+"*"*30)
        print("1) Clientes")
        print("2) Productos")
        print("3) Ventas")
        print("0) Salir")
        a=input("Selecciona una opción: ")
        if(a=='1'):
            ic=InterfaceCliente()
            ic.menuCliente()
        elif(a=='2'):
            ip=InterfaceProducto()
            ip.menuProductos()
        elif(a=='3'):
            iv=InterfaceVentas()
            iv.menuVentas()
        elif(a=='0'):
            break;
        else:
            print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
            input()

if __name__=='__main__':
	menu()