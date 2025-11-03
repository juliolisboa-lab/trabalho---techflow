# src/controllers/tarefa_controller.py
from src.models.tarefa import Tarefa

tarefas = []
contador_id = 1

def criar_tarefa(nome, descricao):
    global contador_id
    tarefa = Tarefa(contador_id, nome, descricao)
    tarefas.append(tarefa)
    contador_id += 1
    return tarefa

def listar_tarefas():
    return tarefas

def editar_tarefa(id, nome=None, descricao=None, status=None):
    for tarefa in tarefas:
        if tarefa.id == id:
            if nome: tarefa.nome = nome
            if descricao: tarefa.descricao = descricao
            if status: tarefa.status = status
            return tarefa
    return None

def deletar_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t.id != id]
