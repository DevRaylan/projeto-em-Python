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
    
    def validar_nome(nome):
        if not nome.strip():  # Verifica se o nome não está vazio
            print("Erro: O nome não pode ser vazio.")
        return None
        return nome
    def validar_idade(idade):
        try:
            idade = int(idade)
            if idade <= 0:
                raise ValueError("Idade deve ser um valor positivo.")
            return idade
        except ValueError as e:
            print(f"Erro: {e}")
            return None
    
    def validar_salario(salario):
        try:
            salario = float(salario)
            if salario <= 0:
                raise ValueError("Salário deve ser um valor positivo.")
            return salario
        except ValueError as e:
            print(f"Erro: {e}")
            return None
    
    def validar_tipo(tipo):
        if tipo.lower() not in ["funcionario", "gerente", "desenvolvedor"]:
            print("Erro: Tipo de funcionário inválido. Escolha entre 'funcionario', 'gerente' ou 'desenvolvedor'.")
            return None
        return tipo.lower()
    
    




