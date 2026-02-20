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
    
def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print('Nenhuma tarefa cadastrada.')
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')
        print(f'Total de tarefas: {len(tarefas)}')
