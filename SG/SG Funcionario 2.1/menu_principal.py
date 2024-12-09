from submenu_backup import submenu_backup
from submenu_funcionario import submenu_funcionario
from empresa import Empresa
import sys
import logging

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('menu_principal.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def exibir_menu_principal():
    print("\n--- Menu Principal ---")
    print("1. Gestão de Funcionarios")
    print("2. Backups")
    print("3. Sair")

def menu_principal():
    empresa = Empresa()  # Instantiate the Empresa class

    while True:
        try:
            exibir_menu_principal()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                submenu_funcionario(empresa)
            elif opcao == "2":
                submenu_backup(empresa)
            elif opcao == "3":
                print("Saindo do sistema...")
                sys.exit(0)
            else:
                print("Opção inválida.")
        except Exception as e:
            logger.error(f"Ocorreu um erro: {e}")
            print(f"Ocorreu um erro: {e}")
