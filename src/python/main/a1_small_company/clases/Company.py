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
        running: bool = 'True'
        while running != 'False':
            calc = calculadora()
            running = calc.ingresar_info()
            if running != 'False' and running != None:

                print(running)


companina = Company()
companina.hacer_calculos()
