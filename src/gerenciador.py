# src/gerenciador.py

class GerenciadorTarefas:
    def __init__(self):
        # Inicia uma lista vazia para armazenar os dicionários de tarefas
        self.tarefas = []

    def adicionar_tarefa(self, id_tarefa, titulo, prioridade):
        """Adiciona uma nova tarefa ao sistema."""
        if not titulo:
            raise ValueError("O título da tarefa não pode ser vazio.")
        tarefa = {
            "id": id_tarefa,
            "titulo": titulo,
            "prioridade": prioridade, # Ex: Alta, Média, Baixa
            "status": "A Fazer"
        }
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        """Retorna todas as tarefas registradas."""
        return self.tarefas

    def atualizar_status(self, id_tarefa, novo_status):
        """Atualiza o status de uma tarefa existente."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["status"] = novo_status
                return tarefa
        return None

    def deletar_tarefa(self, id_tarefa):
        """Remove uma tarefa pelo ID."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                self.tarefas.remove(tarefa)
                return True
        return False