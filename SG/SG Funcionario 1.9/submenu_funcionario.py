from banco_de_dados import adicionar_funcionario, listar_funcionarios, buscar_funcionario, excluir_funcionario, editar_funcionario

def submenu_funcionario(empresa):
    while True:
        print("\n--- Submenu Funcionários ---")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Buscar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Editar Funcionário")
        print("6. Voltar para o Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome do funcionário: ")
            idade = int(input("Digite a idade do funcionário: "))
            salario = float(input("Digite o salário do funcionário: "))
            tipo = input("Digite o tipo do funcionário (Funcionário, Gerente, Desenvolvedor): ")
            departamento = input("Digite o departamento do funcionário (deixe em branco se não aplicável): ")
            linguagem_programacao = input("Digite a linguagem de programação do funcionário (deixe em branco se não aplicável): ")

            # Cria um objeto de funcionário com base no tipo
            if tipo == "Funcionário":
                funcionario = Funcionario(nome, idade, salario)
            elif tipo == "Gerente":
                funcionario = Gerente(nome, idade, salario, departamento)
            elif tipo == "Desenvolvedor":
                funcionario = Desenvolvedor(nome, idade, salario, linguagem_programacao)
            else:
                print("Tipo de funcionário inválido.")
                continue

            adicionar_funcionario(empresa, funcionario)
            print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após adicionar
        elif opcao == "2":
            print(listar_funcionarios(empresa))  # Função de listar funcionários chamada com 'empresa'
        elif opcao == "3":
            busca_por = input("Buscar por (nome/id): ").lower()
            
            if busca_por == "nome":
                nome = input("Digite o nome do funcionário a buscar: ")
                print(buscar_funcionario(empresa, nome=nome))  # Busca por nome
            elif busca_por == "id":
                id_funcionario = int(input("Digite o ID do funcionário a buscar: "))
                print(buscar_funcionario(empresa, id_funcionario=id_funcionario))  # Busca por ID
            else:
                print("Opção inválida.")
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
            print("Opção inválida. Tente novamente.")
