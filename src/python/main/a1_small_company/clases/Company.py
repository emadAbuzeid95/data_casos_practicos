from src.python.main.a1_small_company.clases.calculator import calculadora


class Company():
    def __init__(self):
        print('Creando Company')

    def entrada_cliente(self):
        pass

    def gestion_inventario(self):
        pass

    def gestion_perdidas_y_ganancias(self):
        pass

    def hacer_calculos(self):
        #regresar tupla
        running: bool = True
        while running:
            calc: calculadora = calculadora()
            resultado: int = calc.ingresar_info()
            if resultado is not None:
                print(resultado)
            else:
                running = False


companina = Company()
companina.hacer_calculos()
