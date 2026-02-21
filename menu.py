import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input('\nPressione ENTER para continuar...')

def escolher_opcao():
    print('=' * 30)
    print('  GERENCIADOR DE TAREFAS')
    print('=' * 30)
    print('1 - Adicionar tarefa')
    print('2 - Listar todas')
    print('3 - Listar pendentes')
    print('4 - Listar concluídas')
    print('5 - Marcar como concluída')
    print('6 - Remover tarefa')
    print('7 - Sair')
    print('-' * 30)
    return input('Escolha uma opção: ')