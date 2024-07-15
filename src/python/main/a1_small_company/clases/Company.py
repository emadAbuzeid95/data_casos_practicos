class Company:
    def __init__(self):
        print('Creando Company')
        self.catalogos: dict = {
            1: {'nombre': 'Alicate', 'precio': 12.59},
            2: {'nombre': 'Serrucho', 'precio': 15.45},
            3: {'nombre': 'Martillo', 'precio': 9.99},
            4: {'nombre': 'Broca', 'precio': 2.75},
            5: {'nombre': 'Taladro', 'precio': 89.41}
        }
        self.ventas: list = []
        self.compras: list = []

    def entrada_cliente(self):
        pass

    def gestion_inventario(self):
        pass

    def gestion_perdidas_y_ganancias(self):
        menu_pg = """
        Gestión de Pérdidas y Ganancias
        1) Registrar una venta
        2) Registrar una compra
        3) Reporte de pérdidas y ganancias
        4) Volver al menú principal
        """

        option_pg: int = 0
        while option_pg != 4:
            option_pg: int = int(input(menu_pg))
            match option_pg:
                case 1:
                    print("Catálogo de productos:")
                    for id, detalles in self.catalogos.items():
                        print(f"{id}: {detalles['nombre']}")
                    id: int = int(input("Ingrese el ID del producto: "))
                    cantidad: int = int(input("Ingrese la cantidad: "))
                    if id in self.catalogos:
                        venta: dict = {
                            'id': id,
                            'cantidad': cantidad
                        }
                        self.ventas.append(venta)
                        print("Venta registrada.")
                    else:
                        print("ID de producto no válido.")
                case 2:
                    print("Catálogo de productos:")
                    for id, detalles in self.catalogos.items():
                        print(f"{id}: {detalles['nombre']}")
                    id: int = int(input("Ingrese el ID del producto: "))
                    cantidad: int = int(input("Ingrese la cantidad: "))
                    if id in self.catalogos:
                        compra: dict = {
                            'id': id,
                            'cantidad': cantidad
                        }
                        self.compras.append(compra)
                        print("Compra registrada.")
                    else:
                        print("ID de producto no válido.")
                case 3:
                    print("Reporte de pérdidas y ganancias:")
                    print("Ventas registradas:")
                    for venta in self.ventas:
                        producto = self.catalogos[venta['id']]
                        print(f"{producto['nombre']} - Cantidad: {venta['cantidad']} - Total: {producto['precio'] * venta['cantidad']:.2f}€")

                    print("Compras registradas:")
                    for compra in self.compras:
                        producto = self.catalogos[compra['id']]
                        print(f"{producto['nombre']} - Cantidad: {compra['cantidad']} - Total: {producto['precio'] * compra['cantidad']:.2f}€")

                    total_ventas: float = sum(self.catalogos[venta['id']]['precio'] * venta['cantidad'] for venta in self.ventas)
                    total_compras: float = sum(self.catalogos[compra['id']]['precio'] * compra['cantidad'] for compra in self.compras)
                    ganancia_neta: float = total_ventas - total_compras
                    print(f"Ganancias netas: {ganancia_neta:.2f}€")
                case 4:
                    print("Volviendo al menú principal...")
                case _:
                    print("No es una opción correcta.")

    def hacer_calculos(self):
        pass