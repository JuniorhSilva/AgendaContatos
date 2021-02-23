from agenda import Agenda
from interface import Interface
from tratrarerro import TratarErro
from salvarcontatos import ArquivoExportar
from time import sleep
exportar = ArquivoExportar()
t_erro = TratarErro()
menu = Interface()
agenda = Agenda()
horario = agenda.data_agendamento()
menu.apresentacao()
while True:
    menu.menu()
    agenda.importar_contatos('database.csv')
    exportar.exportar_agenda(agenda.agenda_contatos, 'database.csv')
    decisao_usario = t_erro.tratar_erro_int(input('Digite a opção: '))
    if decisao_usario is not None and 0 <= decisao_usario <= 7:
        if decisao_usario == 1:
            if len(agenda.agenda_contatos) != 0:
                agenda.mostrar_contatos()
            else:
                print('Sem contatos na agenda')
        elif decisao_usario == 2:
            if len(agenda.agenda_contatos) != 0:
                buscar = input(f'Digite o nome do contato: ').title()
                agenda.buscar_contato(buscar)
            else:
                print('Sem contatos na agenda')
        elif decisao_usario == 3:
            adicionar_nome = input('Nome: ').title()
            branco_erro = t_erro.erro_branco_variavel(adicionar_nome)
            if adicionar_nome in agenda.agenda_contatos.keys():
                print(f'Contato {adicionar_nome}, ja existe')
            else:
                if branco_erro is not True:
                    telefone, email, endereco = agenda.add_informacao_contato()
                    agenda.add_contato(
                        adicionar_nome, telefone, email, endereco, horario)
                    exportar.exportar_agenda(
                        agenda.agenda_contatos, 'database.csv', 'Adicionado com Sucesso')

        elif decisao_usario == 4:
            adicionar_nome = input('Editar contato: ').title()
            if adicionar_nome in agenda.agenda_contatos.keys():
                telefone, email, endereco = agenda.add_informacao_contato()
                agenda.editar_contato(
                    adicionar_nome, telefone, email, endereco, horario)
                exportar.exportar_agenda(
                    agenda.agenda_contatos, 'database.csv', 'Editado com Sucesso')
            else:
                print(f'Contato {adicionar_nome} não existe')
        elif decisao_usario == 5:
            delete_contato = input('Nome do contato: ').title()
            if delete_contato in agenda.agenda_contatos.keys():
                agenda.excluir_contato(delete_contato)
                exportar.exportar_agenda(
                    agenda.agenda_contatos, 'database.csv', 'Deletado com Sucesso')
            else:
                print('Contato não existe')
        elif decisao_usario == 6:
            nome_arquivo = input('Digite o nome do arquivo: ')
            exportar.exportar_agenda(
                agenda.agenda_contatos, nome_arquivo, 'Exportado com Sucesso')
        elif decisao_usario == 7:
            arquivo_input = input('Digite o nome do arquivo: ')
            agenda.importar_contatos(
                arquivo_input, 'Contatos importados com sucesso')
        elif decisao_usario == 0:
            print('Saindo...')
            sleep(1.5)
            exit(0)
    else:
        print('Operação inválida')
