from submenu_backup import submenu_backup
from submenu_funcionario import submenu_funcionario
from empresa import Empresa
import sys

def menu_principal():
    empresa = Empresa()  # Instantiate the Empresa class

    while True:
        print("\n--- Menu Principal ---")
        print("1. Gestão de Funcionarios")
        print("2. Backups")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            submenu_funcionario(empresa)
        elif opcao == "2":
            submenu_backup(empresa)
        elif opcao == "3":
            print("Saindo do sistema...")
            sys.exit(0)
        else:
            print("Opção inválida.")
