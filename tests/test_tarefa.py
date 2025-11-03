import sys
import os
# Adiciona a pasta src ao path do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from controllers.tarefa_controller import criar_tarefa, listar_tarefas
