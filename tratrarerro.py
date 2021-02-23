class TratarErro:
    @staticmethod
    def tratar_erro_int(valor):
        try:
            valor = int(valor)
            return valor
        except ValueError:
            valor = None
            return valor

    @staticmethod
    def erro_branco_variavel(valor):
        if not valor == '':
            sequencia = len(valor) * ' '
            if sequencia == valor:
                print('Não pode ficar em branco')
                return True
        else:
            print('Valor não inserido')
            return True
        return False
