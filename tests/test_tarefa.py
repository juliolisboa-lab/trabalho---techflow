# tests/test_tarefa.py

import sys
import os

# Adiciona a pasta src ao path do Python para que os imports funcionem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Agora podemos importar os controllers
from controllers.tarefa_controller import criar_tarefa, listar_tarefas, deletar_tarefa, editar_tarefa

def test_criar_tarefa():
    # Contar tarefas antes
    tarefas_antes = len(listar_tarefas())
    
    # Criar uma tarefa de teste
    criar_tarefa("Tarefa Teste", "Descrição de teste")
    
    # Contar tarefas depois
    tarefas_depois = len(listar_tarefas())
    
    # Verificar se a tarefa foi adicionada
    assert tarefas_depois == tarefas_antes + 1

def test_editar_tarefa():
    # Criar tarefa para editar
    tarefa = criar_tarefa("Editar Teste", "Descrição inicial")
    
    # Editar tarefa
    editar_tarefa(tarefa.id, nome="Tarefa Editada", status="Concluída")
    
    # Verificar se os atributos foram atualizados
    tarefas = listar_tarefas()
    tarefa_editada = next(t for t in tarefas if t.id == tarefa.id)
    assert tarefa_editada.nome == "Tarefa Editada"
    assert tarefa_editada.status == "Concluída"

def test_deletar_tarefa():
    # Criar tarefa para deletar
    tarefa = criar_tarefa("Deletar Teste", "Descrição")
    
    # Deletar tarefa
    deletar_tarefa(tarefa.id)
    
    # Verificar se foi realmente deletada
    tarefas = listar_tarefas()
    ids = [t.id for t in tarefas]
    assert tarefa.id not in ids
