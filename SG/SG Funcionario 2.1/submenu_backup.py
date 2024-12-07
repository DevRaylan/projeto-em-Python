import logging
from banco_de_dados import backup_dados, listar_backups, recuperar_backup

# Cria um logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Cria um formatter para o logger
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Cria um file handler para o logger
file_handler = logging.FileHandler('backups.log')
file_handler.setFormatter(formatter)

# Adiciona o file handler ao logger
logger.addHandler(file_handler)

def submenu_backup(empresa):
    while True:
        print("\n--- Submenu de Backups ---")
        print("1. Listar Backups Armazenados")
        print("2. Criar Backup de Dados")
        print("3. Recuperar Backup de Dados")
        print("4. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_backups()
        elif opcao == "2":
            backup_dados()
        elif opcao == "3":
            recuperar_backup()
        elif opcao == "4":
            break  # Voltar para o menu principal
        else:
            print("Opção inválida.")
