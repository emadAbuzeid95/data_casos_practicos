print("****GESTIÓN DEL INVENTARIO*****")
def pedir_producto():
    for clave, valor in invetario_tienda.items():
        print(clave + ":" + valor["NOMBRE"])
    respuesta:str = input("Escribe la referencia del producto que quieras\n").upper()

    return respuesta

invetario_tienda: dict = {"X1":
                              {"NOMBRE": "Tuercas",
                               "UNIDADES": 4,
                               "PRECIO COMPRA": 2,
                               "PRECIO VENTA": 4,},
                          "X2":
                              {"NOMBRE": "Tornillos",
                                        "UNIDADES": 4,
                                        "PRECIO COMPRA": 6,
                                        "PRECIO VENTA": 6},
                          "X3": {"NOMBRE": "Clavos",
                                     "UNIDADES": 4,
                                     "PRECIO COMPRA": 6,
                                     "PRECIO VENTA": 6},
                          "X4": {"NOMBRE": "Alcayatas",
                                        "UNIDADES": 4,
                                        "PRECIO COMPRA": 6,
                                        "PRECIO VENTA": 6
                                 },
                          "X5": {"NOMBRE": "Pernos",
                                     "UNIDADES": 4,
                                     "PRECIO COMPRA": 6,
                                     "PRECIO VENTA": 6}
                          }

opcion_elegida: int = 0
dinero: int = 100
while opcion_elegida != 5:

    print("""BUENOS DÍAS, ¿QUÉ QUIERE HACER CON EL INVERNTARIO?
            1º Compra de mercancías
            2º Venta de mercancías
            3º Informe del inventario
            4º Saldo en la caja
            5º Salir de gestión inventario""")

    opcion_elegida: int = int(input("Elige una opción con un número entero\n"))
    match opcion_elegida:
        case 1 if dinero > 0:
            print("Estás en la opción compra de inventario.\n Qué producto queremos comprar\n")
            respuesta: str = pedir_producto()
            if respuesta in invetario_tienda:
                cifra_a_gestionar: int = int(input(f"Cuantos {respuesta} quieres comprar?\n"))
                invetario_tienda[respuesta]["UNIDADES"]+=cifra_a_gestionar
                dinero-=(cifra_a_gestionar*invetario_tienda[respuesta]["PRECIO COMPRA"])
            else:
                print("No tienes ese producto")
        case 2:
            print("Estás en la opción venta de inventario\n ¿Qué producto estamos vendiendo?\n")
            respuesta : str = pedir_producto()
            if respuesta in invetario_tienda:
                cifra_a_gestionar: int = int(input(f"Cuantos {respuesta} quieres vender?\n"))
                if invetario_tienda[respuesta]["UNIDADES"] < cifra_a_gestionar:
                    invetario_tienda[respuesta]["UNIDADES"] -= cifra_a_gestionar
                    dinero += (cifra_a_gestionar * invetario_tienda[respuesta]["PRECIO VENTA"])
                else:
                    print(f"No tienes suficientes unidades de {invetario_tienda[respuesta]} para vender")
            else:
                print("No tenemos ese producto")

        case 3:
            print("Estás en la opción visualizar el inventario\n Qué producto quieres ver\n")
            respuesta : str = pedir_producto()
            if respuesta in invetario_tienda:
                print(", ".join(invetario_tienda[respuesta]))
                respuesta_2 : str = input("Escribe el campo que quieras consultar\n").upper()
                print(invetario_tienda[respuesta][respuesta_2])
            else:
                print("No encuentro ese producto. Prueba a escribirlo bien")

        case 4:
            print(f"TIENES EN LA CAJA DE LA COMPAÑÍA {dinero}")


print("HASTA LUEGO!!")
