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

def deletar_backup():
    backups = listar_backups()
    if not backups:
        print("Nenhum backup disponível para deletar.")
        return

    print("\nSelecione o backup que deseja deletar:")
    for i, backup in enumerate(backups, 1):
        print(f"{i}. {backup}")

    try:
        escolha = int(input("Escolha o número do backup: "))
        if 1 <= escolha <= len(backups):
            backup_selecionado = backups[escolha - 1]
            import os
            os.remove(backup_selecionado)
            logger.info(f"Backup deletado: {backup_selecionado}")
            print(f"Backup {backup_selecionado} deletado com sucesso.")
        else:
            print("Escolha inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")

def submenu_backup(empresa):
    while True:
        print("\n--- Submenu de Backups ---")
        print("1. Listar Backups Armazenados")
        print("2. Criar Backup de Dados")
        print("3. Recuperar Backup de Dados")
        print("4. Deletar Backup de Dados")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_backups()
        elif opcao == "2":
            backup_dados()
        elif opcao == "3":
            recuperar_backup()
        elif opcao == "4":
            deletar_backup()
        elif opcao == "5":
            break  # Voltar para o menu principal
        else:
            print("Opção inválida.")
