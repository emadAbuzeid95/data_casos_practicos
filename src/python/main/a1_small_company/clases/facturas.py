productos: dict = {123: {"precio": 0.50, "Nombre": "Tuercas"},
                   132: {"precio": 5.50, "Nombre": "Martillo"},
                   321: {"precio": 1.50, "Nombre": "Bombilla"},
                   213: {"precio": 6, "Nombre": "Pala"}
                   }

opcion: int = 0
total_comprados: dict = {}

while opcion != 5:
    print(""" **      Welcome to Tuerquito Paquito      ** 
    Menú:
    1) Mostrar artículos
    2) Comprar
    4) Ver factura final 
    5) Salir """)

    opcion: int = int(input("Escoja una opción: "))
    print()
    match opcion:
        case 1:
            for clave, valor in productos.items():
                print(f"""Artículo: {valor["Nombre"]} 
                Precio: {valor["precio"]}€
                Código: {clave}
                        """)

        case 2:
            print("""
            *************** Inicie su pedido ***************
            """)
            nombre_cliente: str = str(input("Nombre del cliente: "))
            codigo_producto: int = int(input("Código del producto: "))
            cantidad_producto: int = int(input("Cantidad: "))

            if codigo_producto in productos.keys():
                dicc_compra: dict = {"Código del producto": codigo_producto,
                                     "Cantidad": cantidad_producto
                                     }
                if nombre_cliente in total_comprados.keys():
                    lista_compra_cliente:list = total_comprados[nombre_cliente]
                    lista_compra_cliente.append(dicc_compra)
                    total_comprados[nombre_cliente] = lista_compra_cliente

                else:
                    total_comprados[nombre_cliente] = [dicc_compra]

                print("""
                                Pedido realizado
                                
                                """)


            else:
                print("""
                Código no válido, pruebe otra vez
                """)


        case 4:

            print("""
            ************* Factura Tuerquito Paquito *************
            """)

            for nombre_cliente, lista_compra in total_comprados.items():
                lista_de_total_articulos:list = []
                for dic in lista_compra:
                    cantidad: int = dic["Cantidad"]
                    codigo: int = dic["Código del producto"]
                    if codigo in productos.keys():
                        precio:float = productos[codigo]["precio"]

                        total_articulos:float = cantidad * precio

                        lista_de_total_articulos.append(total_articulos)

                total_final:float = sum(lista_de_total_articulos)

                print(f"""
                        Factura a nombre de Sr/a {nombre_cliente}. {total_final} 
                    
                        """)

        case 5:
            print("""   Ha escogido la opción salir     
                            Hasta la próxima""")

        case _:
            print("Opción no válida")
