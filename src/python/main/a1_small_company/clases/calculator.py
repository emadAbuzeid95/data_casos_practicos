operacion: str = input('operacion\n')
signos = ("+" in operacion, '-' in operacion, '/' in operacion, '*' in operacion)
numeros=operacion.split('+')
if signos[0]==True:
    numeros = operacion.split('+')
    print(int(numeros[0])+int(numeros[1]))
elif signos[1]==True:
    numeros = operacion.split('-')
    print(int(numeros[0])-int(numeros[1]))
elif signos[2]==True:
    numeros = operacion.split('/')
    print(int(numeros[0])/int(numeros[1]))
elif signos[3]==True:
    numeros = operacion.split('*')
    print(int(numeros[0])*int(numeros[1]))


