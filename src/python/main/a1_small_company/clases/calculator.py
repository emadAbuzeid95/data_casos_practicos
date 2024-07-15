class calculadora:

    def calcular(self, operacion, indice_signo):
        if operacion == 'salir':
            return None
        else:
            try:
                match indice_signo:
                    case 0:
                        numeros = operacion.split('+')
                        return float(numeros[0]) + float(numeros[1])
                        #numeros decimanles
                    case 1:
                        numeros = operacion.split('-')
                        return float(numeros[0]) - float(numeros[1])
                    case 2:
                        numeros = operacion.split('*')
                        return float(numeros[0]) * float(numeros[1])
                    case 3:
                        numeros = operacion.split('/')
                        return float(numeros[0]) / float(numeros[1])
                    case _:
                        input('lo sentimos lo que ingresaste no es válido cases')
                        return None
            except:
                input('lo sentimos lo que ingresaste no es válido trais')
                return None

    def ingresar_info(self):

        operacion: str = input('operacion (escribe salir para terminal la operacion)\n')

        signos: tuple = ("+" in operacion, '-' in operacion, '*' in operacion, '/' in operacion)

        try:
            variable: int = signos.index(True)

        except:
            variable: int = 4

        resultado = self.calcular(operacion, variable)

        return resultado
