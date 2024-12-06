#funcionario.py
#classe
class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome  # Atributo de instância
        self.idade = idade
        self.salario = salario

    def exibir_dados(self):
        """Método para exibir os dados do funcionário."""
        return f'Nome: {self.nome}, Idade: {self.idade}, Salário: R${self.salario:.2f}'

    def calcular_bonus(self):
        """Método para calcular o bônus, que é 10% do salário."""
        return self.salario * 0.1
