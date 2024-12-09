from dadosDeFuncionarios import DadosDeFuncionarios as Funcionario

class Assistente(Funcionario):
    def __init__(self, nome, idade, salario, funcao_assistencial):
        super().__init__(nome, idade, salario)
        self.funcao_assistencial = funcao_assistencial

    def exibir_dados(self):
        """Método sobrescrito para exibir dados do assistente com a função assistencial."""
        return f'{super().exibir_dados()}, Função Assistencial: {self.funcao_assistencial}'
