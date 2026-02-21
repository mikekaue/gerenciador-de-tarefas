from menu import escolher_opcao, limpar_tela, pausar
from tarefas import (
    carregar_tarefas,
    salvar_tarefas,
    listar_tarefas,
    filtrar_tarefas
)

tarefas = carregar_tarefas()

while True:
    limpar_tela()
    opcao = escolher_opcao()

    if opcao == '1':
        limpar_tela()
        titulo = input('Digite a tarefa: ').strip()

        if titulo == '':
            print('Tarefa vazia não pode ser adicionada.')
        else:
            tarefas.append({
                'titulo': titulo,
                'concluida': False
            })
            salvar_tarefas(tarefas)
            print('Tarefa adicionada com sucesso.')

        pausar()

    elif opcao == '2':
        limpar_tela()
        listar_tarefas(tarefas)
        pausar()

    elif opcao == '3':
        limpar_tela()
        pendentes = filtrar_tarefas(tarefas, False)
        listar_tarefas(pendentes)
        pausar()

    elif opcao == '4':
        limpar_tela()
        concluidas = filtrar_tarefas(tarefas, True)
        listar_tarefas(concluidas)
        pausar()

    elif opcao == '5':
        limpar_tela()
        listar_tarefas(tarefas)

        if not tarefas:
            pausar()
            continue

        try:
            indice = int(input('\nDigite o número da tarefa concluída: ')) - 1
        except ValueError:
            print('Entrada inválida.')
            pausar()
            continue

        if 0 <= indice < len(tarefas):
            if tarefas[indice]['concluida']:
                print('Essa tarefa já está concluída.')
            else:
                tarefas[indice]['concluida'] = True
                salvar_tarefas(tarefas)
                print('Tarefa marcada como concluída.')
        else:
            print('Número inválido.')

        pausar()

    elif opcao == '6':
        limpar_tela()
        listar_tarefas(tarefas)

        if not tarefas:
            pausar()
            continue

        try:
            indice = int(input('\nDigite o número da tarefa a remover: ')) - 1
        except ValueError:
            print('Entrada inválida.')
            pausar()
            continue

        if 0 <= indice < len(tarefas):
            confirmacao = input(
                f'Remover "{tarefas[indice]["titulo"]}"? (s/n): '
            ).lower()

            if confirmacao == 's':
                tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print('Tarefa removida.')
            else:
                print('Remoção cancelada.')
        else:
            print('Número inválido.')

        pausar()

    elif opcao == '7':
        break

    else:
        print('Opção inválida.')
        pausar()