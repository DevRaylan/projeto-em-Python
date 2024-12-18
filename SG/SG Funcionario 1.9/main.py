from menu_principal import menu_principal
from submenu_funcionario import submenu_funcionario
from banco_de_dados import backup_dados, listar_backups, recuperar_backup
from empresa import Empresa

# Criando a instância da empresa
empresa = Empresa()

# Loop principal do programa
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        submenu_funcionario(empresa)  # Chama o submenu de funcionários
    elif opcao == "2":
        backup_dados()  # Função para criar backup
    elif opcao == "3":
        recuperar_backup()  # Função para recuperar backup
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

