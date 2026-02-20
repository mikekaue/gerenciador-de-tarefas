import json

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
            return tarefas
    except FileNotFoundError:
        return []

def escolher_opcao():
        print('1 - Adicionar tarefa')
        print('2 - Listar tarefas')
        print('3 - Remover tarefa')
        print('4 - Sair')
        opcao = input('Escolha uma opção: ')
        return opcao

def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')
        print(f'Total de tarefas: {len(tarefas)}')

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
        try:
            indice = int(input('Digite o número da tarefa a ser removida: ')) - 1
        except ValueError:
            print('Entrada inválida. Digite um número.')
            continue
            
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            salvar_tarefas(tarefas)
        else:
            print('Número da tarefa inválido. Tente novamente.')

    elif opcao == '4':
        break

    else:
        print('Opção inválida. Tente novamente.')
