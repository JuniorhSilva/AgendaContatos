from pessoa import Pessoa
from datetime import datetime
from time import sleep


class Agenda(Pessoa):
    def __init__(self, telefone=' ', endereco=' ', email=' '):
        super().__init__()
        self.telefone = telefone
        self.endereco = endereco
        self.email = email
        self.data = datetime.now()
        self.agenda_contatos = {}

    def data_agendamento(self):
        horario = self.data
        return horario.strftime('%d/%m/%Y %H:%M')

    def mostrar_contatos(self):
        for contato in self.agenda_contatos:
            self.buscar_contato(contato)

    def buscar_contato(self, buscar_nome):
        if buscar_nome in self.agenda_contatos.keys():
            sleep(0.5)
            print('¬' * 37)
            print(f'Nome: {buscar_nome}\n'
                  f'Telefone: {self.agenda_contatos[buscar_nome]["telefone"]}\n'
                  f'Email: {self.agenda_contatos[buscar_nome]["email"]}\n'
                  f'Endereço: {self.agenda_contatos[buscar_nome]["endereco"]}\n'
                  f'Data do agendamento: {self.agenda_contatos[buscar_nome]["data"]}')
            print('¬' * 37)
        else:
            print(f'Contato {buscar_nome} não existe')

    def editar_contato(self, nome_att, telefone, email, endereco, horario):
        self.add_contato(nome_att, telefone, email, endereco, horario)

    def add_contato(self, nome_add, telefone, email, endereco, horario):
        self.agenda_contatos[nome_add] = {'telefone': telefone, 'email': email,
                                          'endereco': endereco, 'data': horario}

    def excluir_contato(self, chave_contato):
        self.agenda_contatos.pop(chave_contato)

    @staticmethod
    def add_informacao_contato():
        telefone_add = input('Telefone: ').lower()
        email_add = input('Email: ').lower()
        endereco_add = input('Endereço: ').lower()
        return telefone_add, endereco_add, email_add

    def importar_contatos(self, nome_arquivo, msg=''):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                contato_por_linha = arquivo.readlines()
                for linha in contato_por_linha:
                    detalhes = linha.strip().split(',')
                    nome = detalhes[0]
                    telefone = detalhes[1]
                    email = detalhes[2]
                    endereco = detalhes[3]
                    horario = detalhes[4]
                    self.add_contato(nome, telefone, email, endereco, horario)
            print(msg)
        except IndexError:
            print('Sem Contatos para importar')
        except FileNotFoundError:
            print('Arquivo não encontrado')