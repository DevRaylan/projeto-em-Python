#gerente.py
# Subclasses
from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)  # Chama o construtor da classe base
        self.departamento = departamento

    def exibir_dados(self):
        """Método sobrescrito para exibir dados do gerente com o departamento."""
        return f'{super().exibir_dados()}, Departamento: {self.departamento}'

    def calcular_bonus(self):
        """Método sobrescrito para calcular bônus de 20% para gerentes."""
        return self.salario * 0.2
