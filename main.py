import sys
from src.gerenciador import GerenciadorTarefas

# Menu interativo

def exibir_menu():
    print("\n" + "="*30)
    print("      TECHFLOW LOGÍSTICA      ")
    print("="*30)
    print("1. Cadastrar Nova Tarefa")
    print("2. Listar Fluxo de Trabalho")
    print("3. Atualizar Status da Demanda")
    print("4. Remover Tarefa do Sistema")
    print("5. Sair")
    print("="*30)

def main():
    gerenciador = GerenciadorTarefas()
    # Dados iniciais para o sistema não iniciar totalmente vazio
    gerenciador.adicionar_tarefa(1, "Entregar carga Expressa", "Alta")
    gerenciador.adicionar_tarefa(2, "Manutenção do caminhão", "Média")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR TAREFA ---")
            try:
                id_tarefa = len(gerenciador.listar_tarefas()) + 1
                titulo = input("Digite o título/descrição da tarefa: ")
                prioridade = input("Digite a prioridade (Alta/Média/Baixa): ")
                gerenciador.adicionar_tarefa(id_tarefa, titulo, prioridade)
                print("✓ Tarefa cadastrada com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == "2":
            print("\n--- FLUXO DE TRABALHO ATUAL ---")
            tarefas = gerenciador.listar_tarefas()
            if not tarefas:
                print("Nenhuma tarefa cadastrada.")
            for t in tarefas:
                print(f"ID: {t['id']} | {t['titulo']} | Prioridade: {t['prioridade']} | Status: {t['status']}")

        elif opcao == "3":
            print("\n--- ATUALIZAR STATUS ---")
            try:
                id_tarefa = int(input("Digite o ID da tarefa que deseja alterar: "))
                novo_status = input("Novo status (A Fazer / Em Progresso / Concluído): ")
                resultado = gerenciador.atualizar_status(id_tarefa, novo_status)
                if resultado:
                    print("✓ Status atualizado com sucesso!")
                else:
                    print("❌ Tarefa não encontrada.")
            except ValueError:
                print("❌ Erro: Digite um ID numérico válido.")

        elif opcao == "4":
            print("\n--- REMOVER TAREFA ---")
            try:
                id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
                if gerenciador.deletar_tarefa(id_tarefa):
                    print("✓ Tarefa removida com sucesso!")
                else:
                    print("❌ Tarefa não encontrada.")
            except ValueError:
                print("❌ Erro: Digite um ID numérico válido.")

        elif opcao == "5":
            print("\nEncerrando o TechFlow... Até logo!")
            sys.exit()
        else:
            print("❌ Opção inválida. Escolha um número de 1 a 5.")

if __name__ == "__main__":
    main()