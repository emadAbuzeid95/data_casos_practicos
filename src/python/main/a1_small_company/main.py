from src.python.main.a1_small_company.clases.Company import Company
from src.python.main.a1_small_company.utils.const import messaje_init

if __name__ == '__main__':
    small_company: Company = Company()

    option: int = 0
    while option != 5:
        option = int(input(messaje_init))
        match option:
            case 1:
                print('Has seleccionado entrada de cliente')
                small_company.entrada_cliente()
            case 2:
                print('Has seleccionado gestion de inventario')
                small_company.gestion_inventario()
            case 3:
                print('Has seleccionado gestion de perdidas y ganancias')
                small_company.gestion_perdidas_y_ganancias()
            case 4:
                print('Has seleccionado calcular cosas')
                small_company.hacer_calculos()
            case 5:
                print('Hasta luego')
            case _:
                print('No has seleccionado la opcion correcta')
