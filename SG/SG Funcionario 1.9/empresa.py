from banco_de_dados import adicionar_funcionario, listar_funcionarios, buscar_funcionario, excluir_funcionario, editar_funcionario
from funcionario import Funcionario
from gerente import Gerente
from desenvolvedor import Desenvolvedor
from assistente import Assistente  # Importando a nova subclasse

class Empresa:
    def __init__(self):
        # Cria a tabela no banco de dados, se não existir
        from banco_de_dados import criar_tabela
        criar_tabela()

    def adicionar_funcionario(self, funcionario):
        """Adiciona um funcionário à empresa"""
        adicionar_funcionario(funcionario)

    def listar_funcionarios(self):
        """Lista todos os funcionários da empresa"""
        return listar_funcionarios()

    def buscar_funcionario(self, nome=None, id_funcionario=None):
        """Busca um funcionário pelo nome ou ID"""
        return buscar_funcionario(nome, id_funcionario)

    def excluir_funcionario(self, nome):
        """Exclui um funcionário da empresa"""
        return excluir_funcionario(nome)

    def editar_funcionario(self, nome, idade=None, salario=None, departamento=None, linguagem_programacao=None, funcao_assistencial=None):
        """Edita as informações de um funcionário"""
        return editar_funcionario(nome, idade, salario, departamento, linguagem_programacao, funcao_assistencial)
