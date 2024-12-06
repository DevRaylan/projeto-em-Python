from empresa import Empresa
from funcionario import Funcionario
from gerente import Gerente
from desenvolvedor import Desenvolvedor

# Funções de Validação
def validar_nome(nome):
    if nome.strip().lower() == "cancelar":
        return "cancelar"
    if not nome.strip():
        print("Erro: O nome não pode ser vazio.")
        return None
    return nome

def validar_idade(idade):
    if idade.strip().lower() == "cancelar":
        return "cancelar"
    try:
        idade = int(idade)
        if idade <= 0:
            raise ValueError("Idade deve ser um valor positivo.")
        return idade
    except ValueError as e:
        print(f"Erro: {e}")
        return None

def validar_salario(salario):
    if salario.strip().lower() == "cancelar":
        return "cancelar"
    try:
        salario = float(salario)
        if salario <= 0:
            raise ValueError("Salário deve ser um valor positivo.")
        return salario
    except ValueError as e:
        print(f"Erro: {e}")
        return None

def validar_tipo(tipo):
    if tipo.strip().lower() == "cancelar":
        return "cancelar"
    if tipo.lower() not in ["funcionario", "gerente", "desenvolvedor"]:
        print("Erro: Tipo de funcionário inválido. Escolha entre 'funcionario', 'gerente' ou 'desenvolvedor'.")
        return None
    return tipo.lower()

# Função Adicionar Funcionário
def adicionar_funcionario(empresa):
    print("Digite 'cancelar' a qualquer momento para cancelar a operação.")

    # Nome
    nome = input("Nome: ")
    nome = validar_nome(nome)
    if nome == "cancelar":
        print("Operação cancelada.\n")
        return
    if not nome:
        return

    # Idade
    idade = input("Idade: ")
    idade = validar_idade(idade)
    if idade == "cancelar":
        print("Operação cancelada.\n")
        return
    if idade is None:
        return

    # Salário
    salario = input("Salário: ")
    salario = validar_salario(salario)
    if salario == "cancelar":
        print("Operação cancelada.\n")
        return
    if salario is None:
        return

    # Tipo de Funcionário
    tipo = input("Tipo (funcionario/gerente/desenvolvedor): ")
    tipo = validar_tipo(tipo)
    if tipo == "cancelar":
        print("Operação cancelada.\n")
        return
    if tipo is None:
        return

    # Instanciação do Funcionário
    if tipo == "funcionario":
        funcionario = Funcionario(nome, idade, salario)
    elif tipo == "gerente":
        departamento = input("Departamento: ")
        if departamento.strip().lower() == "cancelar":
            print("Operação cancelada.\n")
            return
        funcionario = Gerente(nome, idade, salario, departamento)
    elif tipo == "desenvolvedor":
        linguagem = input("Linguagem de Programação: ")
        if linguagem.strip().lower() == "cancelar":
            print("Operação cancelada.\n")
            return
        funcionario = Desenvolvedor(nome, idade, salario, linguagem)

    # Adicionando à empresa
    empresa.adicionar_funcionario(funcionario)
    print(f"\nFuncionário {nome} adicionado com sucesso!\n")

# Função Listar Funcionários
def listar_funcionarios(empresa):
    print("\nFuncionários da Empresa:")
    print(empresa.listar_funcionarios())

# Função Buscar Funcionário
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

# Função Excluir Funcionário
def excluir_funcionario(empresa):
    nome = input("Digite o nome do funcionário a excluir: ")
    print(empresa.excluir_funcionario(nome))

# Função Editar Funcionário
def editar_funcionario(empresa):
    nome = input("Digite o nome do funcionário a editar: ")
    print("Deixe os campos em branco se não quiser alterar.")
    idade = input("Nova Idade (deixe em branco para não alterar): ")
    salario = input("Novo Salário (deixe em branco para não alterar): ")
    departamento = input("Novo Departamento (deixe em branco para não alterar): ")
    linguagem = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")

    idade = int(idade) if idade else None
    salario = float(salario) if salario else None

    print(empresa.editar_funcionario(nome, idade, salario, departamento, linguagem))

# Função de Menu
def menu():
    print("\n--- Menu ---")
    print("1. Adicionar Funcionário")
    print("2. Listar Funcionários")
    print("3. Buscar Funcionário")
    print("4. Excluir Funcionário")
    print("5. Editar Funcionário")
    print("6. Sair")

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
