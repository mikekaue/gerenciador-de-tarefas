import json

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
        return

    for i, tarefa in enumerate(tarefas, start=1):
        status = '[✔]' if tarefa['concluida'] else '[ ]'
        print(f'{i}. {status} {tarefa["titulo"]}')

    print(f'\nTotal: {len(tarefas)} tarefa(s)')

def filtrar_tarefas(tarefas, status):
    return [tarefa for tarefa in tarefas if tarefa['concluida'] == status]