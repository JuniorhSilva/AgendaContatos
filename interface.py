
class Interface:
    lista_menu = ['mostrar contatos', 'buscar contato',
                  'adicionar contato', 'editar contato',
                  'excluir contato', 'exportar Agenda', 'importar contatos', 'sair']

    def menu(self):
        print('¬' * 25)
        for opcao in range(len(self.lista_menu)):
            if opcao == 7:
                opcao = -1
            print(f'{[opcao+1]}- {self.lista_menu[opcao].upper()}')
        print('¬' * 25)
        print()

    @staticmethod
    def apresentacao():
        print('¬' * 25)
        print('\t AGENDA')
        print('¬' * 25)
        print()