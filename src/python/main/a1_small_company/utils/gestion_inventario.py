print("****GESTIÓN DEL INVENTARIO*****")

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
            3ª Listar productos
            4º Informe del inventario
            5º Saldo en la caja
            6º Salir de gestión inventario""")

    opcion_elegida: int = int(input("Elige una opción con un número entero\n"))
    match opcion_elegida:
        case 1 if dinero > 0:
            ref_producto: str = input("Estás en la opción compra de inventario.\n Qué producto queremos comprar\n").upper()
            if ref_producto in invetario_tienda:
                cifra_a_comprar: int = int(input(f"Cuantos {ref_producto} quieres comprar?\n"))
                if dinero>= (cifra_a_comprar*invetario_tienda[ref_producto]["PRECIO COMPRA"]):
                    dinero-=(cifra_a_comprar*invetario_tienda[ref_producto]["PRECIO COMPRA"])
                else:
                    print("No tienes suficiente dinero para comprar eso")
                invetario_tienda[ref_producto]["UNIDADES"] += cifra_a_comprar
            else:

                print("No tienes ese producto")

        case 2:
            ref_producto : str = input("Estás en la opción venta de inventario\n ¿Qué producto estamos vendiendo?\n").upper()
            if ref_producto in invetario_tienda:
                cifra_a_vender: int = int(input(f"Cuantos {ref_producto} quieres vender?\n"))
                if invetario_tienda[ref_producto]["UNIDADES"] > cifra_a_vender:
                    print(invetario_tienda[ref_producto]["UNIDADES"]+cifra_a_vender)
                    invetario_tienda[ref_producto]["UNIDADES"] -= cifra_a_vender
                    dinero += (cifra_a_vender * invetario_tienda[ref_producto]["PRECIO VENTA"])
                else:
                    print(f"No tienes suficientes unidades de {invetario_tienda[ref_producto]} para vender!")
            else:
                print("No tenemos ese producto")

        case 3:
                for clave, valor in invetario_tienda.items():
                    print(clave + ":" + valor["NOMBRE"])

        case 4:
            ref_producto : str = input(("Estás en la opción visualizar el inventario\n Qué producto quieres ver\n")).upper()
            if ref_producto in invetario_tienda:
                print(", ".join(invetario_tienda[ref_producto]))
                campo_a_consultar : str = input("Escribe el campo que quieras consultar\n").upper()
                print(invetario_tienda[ref_producto][campo_a_consultar])
            else:
                print("No encuentro ese producto. Prueba a escribirlo bien")

        case 5:
            print(f"TIENES EN LA CAJA DE LA COMPAÑÍA {dinero}")
        case 6:
            print("Hasta luego!!")
        case _:
            print("TE HAS EQUIVOCADO DE OPCIÓN")



