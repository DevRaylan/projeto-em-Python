import shutil
from empresa import Empresa
from funcionario import Funcionario
from gerente import Gerente
from desenvolvedor import Desenvolvedor

def menu():
    print("\n--- Menu ---")
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Buscar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Editar Funcionário")
    print("6. Criar Backup de Dados")
    print("7. Recuperar Backup de Dados")
    print("8. Sair")

def adicionar_funcionario(empresa):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    tipo = input("Tipo (funcionario/gerente/desenvolvedor): ").lower()

    if tipo == "funcionario":
        funcionario = Funcionario(nome, idade, salario)
    elif tipo == "gerente":
        departamento = input("Departamento: ")
        funcionario = Gerente(nome, idade, salario, departamento)
    elif tipo == "desenvolvedor":
        linguagem = input("Linguagem de Programação: ")
        funcionario = Desenvolvedor(nome, idade, salario, linguagem)
    else:
        print("Tipo inválido. Funcionário não adicionado.")
        return
    
    empresa.adicionar_funcionario(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso!")

def listar_funcionarios(empresa):
    """Mostra a lista de funcionários no formato tabular"""
    print("\nFuncionários da Empresa:")
    print(empresa.listar_funcionarios())  # Exibe os funcionários com formatação tabular

def buscar_funcionario(empresa):
    busca_por = input("Buscar por (nome/id): ").lower()
    
    if busca_por == "nome":
        nome = input("Digite o nome do funcionário a buscar: ")
        print(empresa.buscar_funcionario(nome=nome))
    elif busca_por == "id":
        id_funcionario = int(input("Digite o ID do funcionário a buscar: "))
        print(empresa.buscar_funcionario(id_funcionario=id_funcionario))
    else:
        print("Opção inválida.")

def excluir_funcionario(empresa):
    try:
        id_funcionario = int(input("Digite o ID do funcionário a excluir: "))
        print(empresa.excluir_funcionario(id_funcionario))
    except ValueError:
        print("ID inválido. Tente novamente.")


def editar_funcionario(empresa):
    try:
        id_funcionario = int(input("Digite o ID do funcionário a editar: "))
        print("Deixe os campos em branco se não quiser alterar.")
        idade = input("Nova Idade (deixe em branco para não alterar): ")
        salario = input("Novo Salário (deixe em branco para não alterar): ")
        departamento = input("Novo Departamento (deixe em branco para não alterar): ")
        linguagem = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")

        idade = int(idade) if idade else None
        salario = float(salario) if salario else None

        print(empresa.editar_funcionario(id_funcionario, idade, salario, departamento, linguagem))
    except ValueError:
        print("Entrada inválida. Tente novamente.")


def criar_backup():
    """Chama a função de backup de dados."""
    backup_dados() # type: ignore

# Corrigindo a função de recuperação de backup
def recuperar_backup():
    """Permite que o usuário recupere um backup a partir de uma lista."""
    backups = listar_backups() # type: ignore

    if not backups:
        return  # Se não houver backups, retorna sem fazer nada

    while True:  # Usar um loop para repetir a tentativa de entrada
        try:
            # Solicita ao usuário escolher qual backup deseja restaurar
            escolha = int(input(f"Escolha o número do backup que deseja restaurar (1-{len(backups)}): "))

            if 1 <= escolha <= len(backups):
                backup_selecionado = backups[escolha - 1]
                # Substitui o banco de dados atual pelo backup selecionado
                shutil.copy(backup_selecionado, 'empresa.db')
                print(f"Backup {backup_selecionado} restaurado com sucesso!")
                break  # Sai do loop após a restauração
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
        except Exception as e:
            print(f"Erro ao restaurar o backup: {e}")
            break  # Encerra o loop em caso de erro



# Criando a instância da empresa
empresa = Empresa()

# Loop principal do programa
while True:
    menu()
    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adicionar_funcionario(empresa)
        elif opcao == 2:
            listar_funcionarios(empresa)
        elif opcao == 3:
            buscar_funcionario(empresa)
        elif opcao == 4:
            excluir_funcionario(empresa)
        elif opcao == 5:
            editar_funcionario(empresa)
        elif opcao == 6:
            criar_backup()
        elif opcao == 7:
            recuperar_backup()
        elif opcao == 8:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
