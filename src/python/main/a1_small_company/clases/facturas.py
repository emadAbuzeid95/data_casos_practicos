#Entrada mostrar

saludo:str = """\t\t**Tuerquito Paquito Agradece tu visita**\n\n
A continuación te mostraré la lista de los productos, con su valor y su código"""


productos =  {"Tuercas": {"precio":0.50, "código": 123},
     "Martillo": {"precio":5.50, "código": 132},
     "Bombilla": {"precio":5.50, "código": 321}
     }


for producto in productos:
    print(producto)
    for i in productos[producto]:
        print(f"{i} : {productos[producto][i]}")

    print("\n")









