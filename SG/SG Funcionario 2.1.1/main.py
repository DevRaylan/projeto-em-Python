from InquirerPy import inquirer
from submenu_funcionario import submenu_funcionario
from banco_de_dados import backup_dados
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
            # Criar menu usando InquirerPy
            opcao = inquirer.select(
                message="Escolha uma opção:",
                choices=[
                    {"name": "Submenu de Funcionários", "value": "1"},
                    {"name": "Criar Backup", "value": "2"},
                    {"name": "Sair do Sistema", "value": "4"},
                ],
                default="1",  # Opção padrão selecionada
            ).execute()  # Mostra o menu e aguarda a seleção do usuário

            # Executar a ação com base na escolha
            if opcao == "1":
                submenu_funcionario(empresa)
                print('\n')  # Linha extra para espaçamento
            elif opcao == "2":
                backup_dados()
                print('\n')  # Linha extra para espaçamento
            elif opcao == "4":
                print("Saindo do sistema...")
                break
        except Exception as e:
            logger.error(f"Ocorreu um erro: {e}")
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
