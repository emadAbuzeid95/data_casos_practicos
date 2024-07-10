class calculadora:

    def calcular(self, operacion, variable):
        match operacion:
            case 'salir':
                return 'False'
            case _:
                match variable:
                    case 0:
                        numeros = operacion.split('+')
                        try:
                            return int(numeros[0]) + int(numeros[1])

                        except:
                            input('lo sentimos lo que ingresaste no es válido')
                    case 1:
                        numeros = operacion.split('-')
                        try:
                            return int(numeros[0]) - int(numeros[1])
                        except:
                            input('lo sentimos lo que ingresaste no es válido')
                    case 2:
                        numeros = operacion.split('*')
                        try:
                            return int(numeros[0]) * int(numeros[1])
                        except:
                            input('lo sentimos lo que ingresaste no es válido')
                    case 3:
                        numeros = operacion.split('/')
                        if numeros[1] == '0':
                            print('No puedes dividir entre cero')
                        else:
                            try:
                                return int(numeros[0]) / int(numeros[1])
                            except:
                                input('lo sentimos lo que ingresaste no es válido')
                    case _:
                        input('lo sentimos lo que ingresaste no es válido')

    def ingresar_info(self):

        operacion: str = input('operacion (escribe salir para terminal la operacion)\n')

        signos: tuple = ("+" in operacion, '-' in operacion, '*' in operacion, '/' in operacion)
        try:
            variable:int = signos.index(True)
        except:
            variable:int = 4

        resultado=self.calcular(operacion, variable)

        return resultado
