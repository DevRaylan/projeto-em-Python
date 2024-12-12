import logging
import sys
from banco_de_dados import listar_funcionarios, adicionar_funcionario, buscar_funcionario, excluir_funcionario, editar_funcionario
from desenvolvedor import Desenvolvedor  # Import the Desenvolvedor class
from InquirerPy import inquirer

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('funcionarios.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def submenu_funcionario(empresa):
    while True:
        # Exibe a lista de funcionários automaticamente
        print(listar_funcionarios(empresa))

        # Menu interativo usando InquirerPy
        opcao = inquirer.select(
            message="--- Menu Funcionários ---",
            choices=[
                {"name": "Atualizar Lista", "value": "1"},
                {"name": "Adicionar", "value": "2"},
                {"name": "Buscar", "value": "3"},
                {"name": "Excluir", "value": "4"},
                {"name": "Editar", "value": "5"},
                {"name": "Voltar para o Menu Principal", "value": "6"},
                {"name": "Sair do Sistema", "value": "0"},
            ],
            default="1",
        ).execute()

        if opcao == "1":
            print(listar_funcionarios(empresa))
        elif opcao == "2":
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
            elif tipo == "desenvolvedor":
                funcionario = Desenvolvedor(nome, idade, salario, linguagem_programacao)
            else:
                print("Tipo de função inválido.")
                continue

            adicionar_funcionario(empresa, funcionario)
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após adicionar
        elif opcao == "3":
            submenu_buscar_funcionario(empresa)
        elif opcao == "4":
            nome = input("Digite o nome do funcionário a excluir: ")
            print(excluir_funcionario(empresa, nome))  # Excluir funcionário
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após excluir
        elif opcao == "5":
            # Exibe a lista de funcionários
            print(listar_funcionarios(empresa))

            # Submenu de edição com InquirerPy
            opcao_editar = inquirer.select(
                message="--- Submenu Editar Funcionário ---",
                choices=[
                    {"name": "Editar por Nome", "value": "1"},
                    {"name": "Editar por ID", "value": "2"},
                    {"name": "Voltar para o Menu Funcionários", "value": "3"},
                ],
                default="1",
            ).execute()

            if opcao_editar == "1":
                nome = input("Digite o nome do funcionário a editar: ")
                idade = input("Nova Idade (deixe em branco para não alterar): ")
                salario = input("Novo Salário (deixe em branco para não alterar): ")
                departamento = input("Novo Departamento (deixe em branco para não alterar): ")
                linguagem_programacao = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")

                idade = int(idade) if idade else None
                salario = float(salario) if salario else None

                resultado = editar_funcionario(empresa, nome=nome, idade=idade, salario=salario, departamento=departamento, linguagem_programacao=linguagem_programacao)  # Editar funcionário
                print(resultado)
            elif opcao_editar == "2":
                try:
                    id_funcionario = int(input("Digite o ID do funcionário a editar: "))
                    idade = input("Nova Idade (deixe em branco para não alterar): ")
                    salario = input("Novo Salário (deixe em branco para não alterar): ")
                    departamento = input("Novo Departamento (deixe em branco para não alterar): ")
                    linguagem_programacao = input("Nova Linguagem de Programação (deixe em branco para não alterar): ")

                    idade = int(idade) if idade else None
                    salario = float(salario) if salario else None

                    resultado = editar_funcionario(empresa, id_funcionario=id_funcionario, idade=idade, salario=salario, departamento=departamento, linguagem_programacao=linguagem_programacao)  # Editar funcionário
                    print(resultado)
                    print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários atualizada após editar
                except ValueError as e:
                    logger.error(f"Ocorreu um erro: {e}")
                    print(f"Ocorreu um erro: {e}. Voltando para o menu principal.")
            elif opcao_editar == "3":
                continue  # Voltar para o menu principal
            else:
                print("Opção inválida.")
        elif opcao == "6":
            break  # Voltar para o menu principal
        elif opcao == "0":
            print("Saindo do sistema...")
            sys.exit(0)
        else:
            print("Opção inválida.")

def submenu_buscar_funcionario(empresa):
    while True:
        # Submenu de busca com InquirerPy
        opcao = inquirer.select(
            message="--- Submenu Buscar Funcionário ---",
            choices=[
                {"name": "Buscar por Nome", "value": "1"},
                {"name": "Buscar por ID", "value": "2"},
                {"name": "Voltar para o Menu Funcionários", "value": "3"},
            ],
            default="1",
        ).execute()

        if opcao == "1":
            nome = input("Digite o nome do funcionário a buscar: ")
            logger.info(f"Buscando funcionário por nome: {nome}")
            result = buscar_funcionario(empresa, nome=nome)
            logger.info(f"Resultado da busca por nome: {result}")
            print(result)  # Busca por nome
        elif opcao == "2":
            try:
                id_funcionario = int(input("Digite o ID do funcionário a buscar: "))
                logger.info(f"Buscando funcionário por ID: {id_funcionario}")
                result = buscar_funcionario(empresa, id_funcionario=id_funcionario)
                logger.info(f"Resultado da busca por ID: {result}")
                print(result)  # Busca por ID
            except ValueError as e:
                logger.error(f"Ocorreu um erro: {e}")
                print(f"Ocorreu um erro: {e}. Voltando para o menu principal.")
                break
        elif opcao == "3":
            break  # Voltar para o menu principal
        else:
            print("Opção inválida.")
