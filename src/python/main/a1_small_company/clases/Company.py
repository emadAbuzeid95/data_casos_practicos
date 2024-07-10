class Company():
    def __init__(self):
        print('Creando Company')

    def entrada_cliente(self):
        pass

    def gestion_inventario(self):
        pass

    def gestion_perdidas_y_ganancias(self):
        menu_pg: str = """
        Gestión de Pérdidas y Ganancias
        1) Registrar una venta
        2) Registrar una compra
        3) Reporte de pérdidas y ganancias
        4) Volver al menú principal

        """

        self.ventas: list = []
        self.compras: list = []

        option_pg: int = 0
        while option_pg != 4:
            option_pg: int = int(input(menu_pg))
            match option_pg:
                case 1:
                    producto: str = str(input("Ingrese el nombre del producto: "))
                    cantidad: int = int(input("Ingrese la cantidad: "))
                    precio_v: float = float(input("Ingrese el precio de venta: "))
                    venta = {
                        'producto': producto,
                        'cantidad': cantidad,
                        'precio_v': precio_v
                    }
                    self.ventas.append(venta)
                    print("Venta registrada.")
                case 2:
                    producto: str = str(input("Ingrese el nombre del producto: "))
                    cantidad: int = int(input("Ingrese la cantidad: "))
                    precio_c: float = float(input("Ingrese el precio de compra: "))
                    compra = {
                        'producto': producto,
                        'cantidad': cantidad,
                        'precio_c': precio_c
                    }
                    self.compras.append(compra)
                    print("Compra registrada.")
                case 3:
                    print("Reporte de pérdidas y ganancias:")
                    print("Ventas registradas:")
                    for venta in self.ventas:
                        print(venta)
                    print("Compras registradas:")
                    for compra in self.compras:
                        print(compra)
                    total_v: float = sum(venta['precio_v'] * venta['cantidad'] for venta in self.ventas)
                    total_c: float = sum(compra['precio_c'] * compra['cantidad'] for compra in self.compras)
                    ganancia: float = total_v - total_c
                    print(f"Ganancias netas: {ganancia:.2f}")
                case 4:
                    print("Volviendo al menú principal...")
                case _:
                    print("No es una opcion correcta Griezman.")

    def hacer_calculos(self):
        pass
