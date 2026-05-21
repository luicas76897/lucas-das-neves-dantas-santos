agendamentos = []


def listar_agendamentos():
    if not agendamentos:
        print('Nenhum agendamento.')
        return
    for i, item in enumerate(agendamentos, 1):
        print(f"{i}. {item['titulo']} - {item['data']} {item['hora']} - {item['descricao']}")


def adicionar_agendamento():
    titulo = input('Título: ')
    data = input('Data (dd/mm/aaaa): ')
    hora = input('Hora (hh:mm): ')
    descricao = input('Descrição: ')
    agendamentos.append({
        'titulo': titulo,
        'data': data,
        'hora': hora,
        'descricao': descricao,
    })
    print('Agendamento adicionado!')


def remover_agendamento():
    listar_agendamentos()
    if not agendamentos:
        return
    try:
        idx = int(input('Número do agendamento para remover: '))
        if 1 <= idx <= len(agendamentos):
            removido = agendamentos.pop(idx - 1)
            print('Removido:', removido['titulo'])
        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida.')


def menu():
    while True:
        print('\nOpções:')
        print('1 - Adicionar')
        print('2 - Remover')
        print('3 - Ver a lista')
        print('4 - Finalizar')
        opc = input('Escolha uma opção: ')

        if opc == '1':
            adicionar_agendamento()
        elif opc == '2':
            remover_agendamento()
        elif opc == '3':
            listar_agendamentos()
        elif opc == '4':
            print('Agendamento finalizado!')
            break
        else:
            print('Opção inválida.')


if __name__ == '__main__':
    menu()
 

    

