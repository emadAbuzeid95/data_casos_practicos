print("****GESTIÓN DEL INVENTARIO*****")
invetario_tienda: dict = {"Tuercas": 0, "Tornillos": 0, "Clavos": 0, "Alcayatas": 0, "Pernos": 0}
dict_precio_compra: dict = {"Tuercas": 2, "Tornillos": 4, "Clavos": 6, "Alcayatas": 6, "Pernos": 6}
dict_precio_venta: dict = {"Tuercas": 3, "Tornillos": 6, "Clavos": 8, "Alcayatas": 10, "Pernos": 12}
opcion_elegida: int = 0
dinero: int = 100
while opcion_elegida != 5:

    print("BUENOS DÍAS, ¿QUÉ QUIERE HACER CON EL INVERNTARIO?")
    print("1º Compra de mercancías")
    print("2º Venta de mercancías")
    print("3º Informe del inventario")
    print("4º Saldo en la caja")
    print("5º Salir de gestión inventario")
    opcion_elegida: int = int(input("Elige una opción con un número entero\n"))
    match opcion_elegida:
        case 1 if dinero > 0:
            print("Estás en la opción compra de inventario.\n Qué producto queremos comprar")
            print(invetario_tienda.keys())
            respuesta = input("Escribe el producto que quieras\n")
            match respuesta:
                case "Tuercas":
                    cifra_a_gestionar: int = int(input("Cuantos quieres comprar"))
                    invetario_tienda["Tuercas"] += cifra_a_gestionar
                    dinero -= (dict_precio_compra["Tuercas"]*cifra_a_gestionar)

                case "Tornillos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres comprar"))
                    invetario_tienda["Tornillos"] += cifra_a_gestionar
                    dinero -= dict_precio_compra["Tuercas"]*cifra_a_gestionar

                case "Clavos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres comprar"))
                    invetario_tienda["Clavos"] += cifra_a_gestionar
                    dinero -= dict_precio_compra["Tuercas"]*cifra_a_gestionar

                case "Alcayatas":
                    cifra_a_gestionar: int = int(input("Cuantos quieres comprar"))
                    invetario_tienda["Alcayatas"] += cifra_a_gestionar
                    dinero -= dict_precio_compra["Tuercas"]*cifra_a_gestionar

                case "Pernos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres comprar"))
                    invetario_tienda["Pernos"] += cifra_a_gestionar
                    dinero -= dict_precio_compra["Tuercas"]*cifra_a_gestionar

        case 2:
            print("Estás en la opción venta de inventario\n ¿Qué producto estamos vendiendo?")
            print(invetario_tienda.keys())
            respuesta = input("Escribe el producto que quieras\n")
            match respuesta:
                case "Tuercas":
                    cifra_a_gestionar: int = int(input("Cuantos quieres vender"))
                    invetario_tienda["Tuercas"] -= cifra_a_gestionar
                    dinero += dict_precio_venta["Tuercas"]*cifra_a_gestionar
                case "Tornillos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres vender"))
                    invetario_tienda["Tornillos"] -= cifra_a_gestionar
                    dinero += dict_precio_venta["Tornillos"]*cifra_a_gestionar
                case "Clavos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres vender"))
                    invetario_tienda["Clavos"] -= cifra_a_gestionar
                    dinero += dict_precio_venta["Clavos"]*cifra_a_gestionar
                case "Alcayatas":
                    cifra_a_gestionar: int = int(input("Cuantos quieres vender"))
                    invetario_tienda["Alcayatas"] -= cifra_a_gestionar
                    dinero += dict_precio_venta["Alcayatas"]*cifra_a_gestionar
                case "Pernos":
                    cifra_a_gestionar: int = int(input("Cuantos quieres vender"))
                    invetario_tienda["Pernos"] -= cifra_a_gestionar
                    dinero += dict_precio_venta["Pernos"]*cifra_a_gestionar

        case 3:
            print("Estás en la opción visualizar el inventario\n Qué producto quieres ver")
            print(invetario_tienda.keys())
            respuesta = input("Escribe el producto que quieras\n")
            match respuesta:
                case "Tuercas":
                    print(invetario_tienda["Tuercas"])
                case "Tornillos":
                    print(invetario_tienda["Tornillos"])
                case "Clavos":
                    print(invetario_tienda["Tuercas"])
                case "Alcayatas":
                    print(invetario_tienda["Alcayatas"])
                case "Pernos":
                    print(invetario_tienda["Pernos"])
        case 4:
            print(f"TIENES EN LA CAJA DE LA COMPAÑÍA {dinero}")

print("HASTA LUEGO!!")
