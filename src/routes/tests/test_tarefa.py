# tests/test_tarefa.py
from src.controllers.tarefa_controller import criar_tarefa, listar_tarefas

def test_criar_tarefa():
    tarefas = listar_tarefas()
    total_antes = len(tarefas)
    criar_tarefa("Testar função", "Descrição de teste")
    tarefas_depois = listar_tarefas()
    assert len(tarefas_depois) == total_antes + 1
