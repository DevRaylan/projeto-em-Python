import logging
from banco_de_dados import listar_funcionarios, adicionar_funcionario, buscar_funcionario, excluir_funcionario, editar_funcionario
from desenvolvedor import Desenvolvedor  # Import the Desenvolvedor class

# Cria um logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Cria um formatter para o logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Cria um file handler para o logger
file_handler = logging.FileHandler('funcionarios.log')
file_handler.setFormatter(formatter)

# Adiciona o file handler ao logger
logger.addHandler(file_handler)

def submenu_buscar_funcionario(empresa):
    while True:
        print("\n--- Submenu Buscar Funcionário ---")
        print("1. Buscar por Nome")
        print("2. Buscar por ID")
        print("3. Voltar para o Menu Funcionários")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do funcionário a buscar: ")
            logger.info(f"Buscando funcionário por nome: {nome}")
            result = buscar_funcionario(empresa, nome=nome)
            logger.info(f"Resultado da busca por nome: {result}")
            print(result)  # Busca por nome
        elif opcao == "2":
            id_funcionario = int(input("Digite o ID do funcionário a buscar: "))
            logger.info(f"Buscando funcionário por ID: {id_funcionario}")
            result = buscar_funcionario(empresa, id_funcionario=id_funcionario)
            logger.info(f"Resultado da busca por ID: {result}")
            print(result)  # Busca por ID
        elif opcao == "3":
            break  # Voltar para o menu principal
        else:
            print("Opção inválida.")

def submenu_funcionario(empresa):
    while True:
        print("\n--- Menu Funcionários ---")
        print("1. Adicionar")
        print("2. Listar ")
        print("3. Buscar ")
        print("4. Excluir ")
        print("5. Editar ")
        print("6. Voltar para o Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            idade = int(input("Digite a idade: "))
            salario = float(input("Digite o salário: "))
            tipo = input("Digite o tipo de função (Geral, Gerente, Desenvolvedor): ").strip().lower()
            departamento = input("Digite o departamento (deixe em branco se não aplicável): ")
            linguagem_programacao = input("Digite a linguagem de programação (deixe em branco se não aplicável): ")

            # Cria um objeto de funcionário com base no tipo
            if tipo == "geral":
                funcionario = Funcionario(nome, idade, salario)
            elif tipo == "gerente":
                funcionario = Gerente(nome, idade, salario, departamento)
            elif tipo == "Desenvolvedor":
                funcionario = Desenvolvedor(nome, idade, salario, linguagem_programacao)
            else:
                print("Tipo de função inválido.")
                continue

            adicionar_funcionario(empresa, funcionario)
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após adicionar
        elif opcao == "2":
            print(listar_funcionarios(empresa))  # Função de listar funcionários chamada com 'empresa'
        elif opcao == "3":
            submenu_buscar_funcionario(empresa)
        elif opcao == "4":
            nome = input("Digite o nome do funcionário a excluir: ")
            print(excluir_funcionario(empresa, nome))  # Excluir funcionário
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após excluir
        elif opcao == "5":
            nome = input("Digite o nome do funcionário a editar: ")
            idade = input("Nova Idade (deixe em branco para não alterar): ")
            salario = input("Novo Salário (deixe em branco para não alterar): ")
            departamento = input("Novo Departamento (deixe em branco para não alterar): ")
            linguagem = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")
            
            idade = int(idade) if idade else None
            salario = float(salario) if salario else None

            print(editar_funcionario(empresa, nome, idade, salario, departamento, linguagem))  # Editar funcionário
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após editar
        elif opcao == "6":
            break  # Voltar para o menu principal
        else:
            print("Opção inválida.")
