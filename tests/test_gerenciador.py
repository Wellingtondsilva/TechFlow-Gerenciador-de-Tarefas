# tests/test_gerenciador.py
import pytest
from src.gerenciador import GerenciadorTarefas

def test_adicionar_tarefa_sucesso():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.adicionar_tarefa(1, "Entregar carga Expressa", "Alta")
    assert tarefa["titulo"] == "Entregar carga Expressa"
    assert len(gerenciador.listar_tarefas()) == 1

def test_adicionar_tarefa_sem_titulo_deve_falhar():
    gerenciador = GerenciadorTarefas()
    # Garante que o sistema barra títulos vazios (validação de entrada)
    with pytest.raises(ValueError):
        gerenciador.adicionar_tarefa(2, "", "Baixa")