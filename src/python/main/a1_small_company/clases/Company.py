from src.python.main.a1_small_company.clases.Calculator import Calculadora


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
            calc: Calculadora = Calculadora()
            resultado: int = calc.ingresar_info()
            if resultado is None:
                running = False
            else:
                print(resultado)


companina = Company()
companina.hacer_calculos()
