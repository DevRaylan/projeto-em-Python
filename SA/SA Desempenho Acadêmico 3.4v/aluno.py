from professor import Professor

class Aluno(Professor):
    def __init__(self, nome, disciplina, codigo_disciplina, notas, ano):
        # Passando os parâmetros para o construtor de Professor
        super().__init__(nome, disciplina, codigo_disciplina, ano)
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def situacao(self):
        media = self.calcular_media()
        return "Aprovado" if media >= 6 else "Reprovado"
