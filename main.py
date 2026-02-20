from menu import escolher_opcao

from tarefas import salvar_tarefas, carregar_tarefas, listar_tarefas

tarefas = carregar_tarefas()

while True:
    
    opcao = escolher_opcao()

    if opcao == '1':
        tarefa = input('Digite a tarefa: ')
        if tarefa.strip() == '':
            print('Tarefa vazia não pode ser adicionada.')
        else:
            tarefas.append(tarefa)
            salvar_tarefas(tarefas)

    elif opcao == '2':
        listar_tarefas(tarefas)

    elif opcao == '3':
        listar_tarefas(tarefas)

        if len(tarefas) == 0:
            continue

        try:
            indice = int(input('Digite o número da tarefa a ser removida: ')) - 1
        except ValueError:
            print('Entrada inválida. Digite um número.')
            continue
            
        if 0 <= indice < len(tarefas):
            tarefa_escolhida = tarefas[indice]
            print(f'Você escolheu remover a tarefa: "{tarefa_escolhida}')

            confirmacao = input('Confirmar remoção? (s/n): ').lower()

            if confirmacao == 's':
                tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print('Tarefa removida com sucesso.')
            else:
                print('Remoção cancelada.')
        else:
            print('Número da tarefa inválido. Tente novamente.')

    elif opcao == '4':
        break

    else:
        print('Opção inválida. Tente novamente.')
