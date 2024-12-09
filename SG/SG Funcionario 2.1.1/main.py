from menu_principal import menu_principal
from submenu_funcionario import submenu_funcionario
from banco_de_dados import backup_dados, listar_backups, recuperar_backup
from empresa import Empresa
import logging

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    # Criando a instância da empresa
    empresa = Empresa()

    # Loop principal do programa
    while True:
        try:
            menu_principal()
            opcao = input("Escolha uma opção: ").strip()  # Remove any leading/trailing whitespace
            
            if opcao == "1":
                submenu_funcionario(empresa)  # Chama o submenu de funcionários
            elif opcao == "2":
                backup_dados()  # Função para criar backup
            elif opcao == "4":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            logger.error(f"Ocorreu um erro: {e}")
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()

