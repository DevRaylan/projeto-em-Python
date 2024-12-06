
# Subclasses
from funcionario import Funcionario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, idade, salario, linguagem_programacao):
        super().__init__(nome, idade, salario)
        self.linguagem_programacao = linguagem_programacao

    def exibir_dados(self):
        """Método sobrescrito para exibir dados do desenvolvedor com a linguagem de programação."""
        return f'{super().exibir_dados()}, Linguagem de Programação: {self.linguagem_programacao}'
