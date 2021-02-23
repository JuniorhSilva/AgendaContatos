class ArquivoExportar:

    @staticmethod
    def exportar_agenda(agenda_local, nome_arquivo, msg=''):
        try:
            with open(nome_arquivo, 'w') as arquivos:
                for contato in agenda_local:
                    telefone = agenda_local[contato]['telefone']
                    email = agenda_local[contato]['email']
                    endereco = agenda_local[contato]['endereco']
                    horario = agenda_local[contato]['data']
                    arquivos.write(f'{contato},{telefone},{email},{endereco},{horario}\n')
                print(msg)
        except FileNotFoundError:
            print('Arquivo não exportado')
