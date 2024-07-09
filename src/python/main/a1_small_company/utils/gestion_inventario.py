print("****GESTIÓN DEL INVENTARIO*****")
invetario_tienda: dict= {"Tuercas":0, "Tornillos":0, "Clavos":0,"Alcayatas":0,"Pernos":0}


print("BUENOS DÍAS, ¿QUÉ QUIERE HACER CON EL INVERNTARIO?")
print("1º Compra de mercancías")
print("2º Venta de mercancías")
print("3º Informe del inventario")
opcion_elegida: int = int(input("Elige una opción con un número entero\n"))

match opcion_elegida:
    case 1:
        print("Estas en la opción compra de inventario")
        int(input("Qué "))

