# src/routes/tarefa_routes.py
from src.controllers.tarefa_controller import criar_tarefa, listar_tarefas

# Criando tarefas de exemplo
criar_tarefa("Comprar leite", "Comprar leite no mercado")
criar_tarefa("Estudar GitHub", "Ler documentação oficial")

# Listando tarefas
for t in listar_tarefas():
    print(f"{t.id}: {t.nome} - {t.status}")
