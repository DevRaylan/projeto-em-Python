def submenu_funcionario(empresa):
    while True:
        # Exibe a lista de funcionários automaticamente
        funcionarios = listar_funcionarios(empresa)
        print(funcionarios)

        # Menu interativo usando InquirerPy
        opcao = inquirer.select(
            message="--- Menu Funcionários ---",
            choices=[
                {"name": "Atualizar Lista", "value": "1"},
                {"name": "Adicionar", "value": "2"},
                {"name": "Buscar", "value": "3"},
                {"name": "Editar ou Excluir Funcionário", "value": "4"},
                {"name": "Voltar para o Menu Principal", "value": "5"},
                {"name": "Sair do Sistema", "value": "0"},
            ],
            default="1",
        ).execute()

        if opcao == "1":
            funcionarios = listar_funcionarios(empresa)
            print(funcionarios)  # Exibe a tabela de funcionários
        elif opcao == "2":
            # Adicionar funcionário
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
            # Menu de seleção de funcionário para editar ou excluir
            funcionarios = listar_funcionarios(empresa)
            if not funcionarios:
                print("Nenhum funcionário encontrado.")
                continue

            # Adiciona navegação por ID
            funcionario_ids = [f"{funcionario['nome']} (ID: {funcionario['id']})" for funcionario in funcionarios]
            
            index_atual = 0  # Começa com o primeiro funcionário

            while True:
                # Exibe o funcionário atual
                funcionario_selecionado = funcionario_ids[index_atual]
                print(f"Funcionario Atual: {funcionario_selecionado}")
                
                # Pergunta ao usuário o que fazer
                opcao_funcionario = inquirer.select(
                    message="O que deseja fazer com o funcionário?",
                    choices=[
                        {"name": "Próximo Funcionário", "value": "1"},
                        {"name": "Funcionário Anterior", "value": "2"},
                        {"name": "Editar", "value": "3"},
                        {"name": "Excluir", "value": "4"},
                        {"name": "Voltar", "value": "5"},
                    ],
                ).execute()

                if opcao_funcionario == "1":  # Próximo funcionário
                    if index_atual < len(funcionario_ids) - 1:
                        index_atual += 1
                    else:
                        print("Você já está no último funcionário.")
                elif opcao_funcionario == "2":  # Funcionário anterior
                    if index_atual > 0:
                        index_atual -= 1
                    else:
                        print("Você já está no primeiro funcionário.")
                elif opcao_funcionario == "3":  # Editar
                    id_funcionario_selecionado = funcionarios[index_atual]['id']
                    editar_funcionario(empresa, id_funcionario=id_funcionario_selecionado)
                elif opcao_funcionario == "4":  # Excluir
                    id_funcionario_selecionado = funcionarios[index_atual]['id']
                    excluir_funcionario(empresa, id_funcionario=id_funcionario_selecionado)
                    print(listar_funcionarios(empresa))  # Exibe a tabela de funcionários após excluir
                elif opcao_funcionario == "5":  # Voltar
                    break
                else:
                    print("Opção inválida.")
        elif opcao == "5":
            break  # Voltar para o menu principal
        elif opcao == "0":
            print("Saindo do sistema...")
            sys.exit(0)
        else:
            print("Opção inválida.")
