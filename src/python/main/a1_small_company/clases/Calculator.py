class Calculadora:

    def calcular(self, operacion: str, indice_signo: int) -> float:
        if operacion == 'salir':
            return None
        else:
            try:
                match indice_signo:
                    case 0:
                        numeros:list = operacion.split('+')
                        return float(numeros[0]) + float(numeros[1])
                        #numeros decimanles
                    case 1:
                        numeros:list = operacion.split('-')
                        return float(numeros[0]) - float(numeros[1])
                    case 2:
                        numeros:list = operacion.split('*')
                        return float(numeros[0]) * float(numeros[1])
                    case 3:
                        numeros:list = operacion.split('/')
                        return float(numeros[0]) / float(numeros[1])
                    case _:
                        print('lo sentimos lo que ingresaste no es válido')
                        return None
            except:
                print('lo sentimos lo que ingresaste no es válido')
                return None

    def ingresar_info(self)->float:

        operacion: str = input('operacion (escribe salir para terminal la operacion)\n')

        signos: tuple = ("+" in operacion, '-' in operacion, '*' in operacion, '/' in operacion)

        try:
            resultado:float = self.calcular(operacion, signos.index(True))
        except:
            print('lo sentimos lo que ingresaste no es válido')
            return None

        return resultado
