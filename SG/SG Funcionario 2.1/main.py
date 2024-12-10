from menu_principal import menu_principal
from submenu_funcionario import submenu_funcionario
from banco_de_dados import backup_dados, listar_backups, recuperar_backup
from empresa import Empresa
import logging
import sys


def verificar_ambiente_virtual():
    """Exibe informações sobre o ambiente virtual."""
    print(f"sys.prefix: {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")


# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('main.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def show_interface(empresa):
    """Implementa a interface da opção 3 (placeholder)."""
    print("Interface de gerenciamento da empresa ainda não implementada.")


def main():
    """Função principal do programa."""
    # Verificar ambiente virtual (opcional, para depuração)
    verificar_ambiente_virtual()

    # Criando a instância da empresa
    empresa = Empresa()

    # Loop principal do programa
    while True:
        try:
            menu_principal()
            opcao = input("Escolha uma opção: ").strip()  # Remove espaços extras

            # Validação da entrada
            if not opcao.isdigit():
                print("Por favor, insira um número válido.")
                continue

            opcao = int(opcao)

            # Processar opções
            if opcao == 1:
                submenu_funcionario(empresa)  # Chama o submenu de funcionários
            elif opcao == 2:
                backup_dados()  # Função para criar backup
            elif opcao == 3:
                show_interface(empresa)  # Interface da opção 3
            elif opcao == 4:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            logger.error(f"Ocorreu um erro: {e}")
            print(f"Ocorreu um erro: {e}")
        finally:
            # Exemplo de encerramento seguro (caso necessário liberar recursos)
            pass


if __name__ == "__main__":
    main()
