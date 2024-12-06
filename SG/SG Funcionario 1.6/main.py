from empresa import Empresa
from funcionario import Funcionario
from gerente import Gerente
from desenvolvedor import Desenvolvedor
from assistente import Assistente  # Importando a nova subclasse

def menu():
    print("\n--- Menu ---")
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Buscar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Editar Funcionário")
    print("6. Sair")

def adicionar_funcionario(empresa):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    salario = float(input("Salário: "))
    tipo = input("Tipo (funcionario/gerente/desenvolvedor/assistente): ").lower()

    if tipo == "funcionario":
        funcionario = Funcionario(nome, idade, salario)
    elif tipo == "gerente":
        departamento = input("Departamento: ")
        funcionario = Gerente(nome, idade, salario, departamento)
    elif tipo == "desenvolvedor":
        linguagem = input("Linguagem de Programação: ")
        funcionario = Desenvolvedor(nome, idade, salario, linguagem)
    elif tipo == "assistente":
        funcao_assistencial = input("Função Assistencial: ")
        funcionario = Assistente(nome, idade, salario, funcao_assistencial)
    else:
        print("Tipo inválido. Funcionário não adicionado.")
        return
    
    empresa.adicionar_funcionario(funcionario)
    print(f"Funcionário {nome} adicionado com sucesso!")

def listar_funcionarios(empresa):
    print("\nFuncionários da Empresa:")
    print(empresa.listar_funcionarios())

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
    nome = input("Digite o nome do funcionário a excluir: ")
    print(empresa.excluir_funcionario(nome))

def editar_funcionario(empresa):
    nome = input("Digite o nome do funcionário a editar: ")
    print("Deixe os campos em branco se não quiser alterar.")
    idade = input("Nova Idade (deixe em branco para não alterar): ")
    salario = input("Novo Salário (deixe em branco para não alterar): ")
    departamento = input("Novo Departamento (deixe em branco para não alterar): ")
    linguagem = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")
    funcao_assistencial = input("Nova Função Assistencial (deixe em branco para não alterar): ")

    idade = int(idade) if idade else None
    salario = float(salario) if salario else None

    print(empresa.editar_funcionario(nome, idade, salario, departamento, linguagem, funcao_assistencial))

# Criando a instância da empresa
empresa = Empresa()

# Loop principal do programa
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_funcionario(empresa)
    elif opcao == "2":
        listar_funcionarios(empresa)
    elif opcao == "3":
        buscar_funcionario(empresa)
    elif opcao == "4":
        excluir_funcionario(empresa)
    elif opcao == "5":
        editar_funcionario(empresa)
    elif opcao == "6":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
