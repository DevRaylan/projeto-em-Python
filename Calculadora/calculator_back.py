# -*- coding:utf-8 -*-
from math import sqrt, factorial

class Calculator:
    def __init__(self):
        self.show = ""

    # Função que adiciona o valor do botão pressionado ao display
    def btnPress(self, num):
        if self.show == "0":
            self.show = ""
        self.show += str(num)
    
    # Função que faz o cálculo da equação
    def evaluate(self):
        try:
            total = str(eval(self.show))
            if len(total) > 20:
                total = total[:20]
            return total
        except Exception:
            return "Erro"
    
    # Função que limpa o display
    def clear(self):
        self.show = "0"
    
    # Função que calcula o fatorial
    def fatorial(self):
        try:
            num = int(self.show)
            if num < 0:
                return "Erro"
            return str(factorial(num))
        except ValueError:
            return "Erro"
    
    # Função que calcula a raiz quadrada
    def raiz(self):
        try:
            num = float(self.show)
            return str(sqrt(num))
        except ValueError:
            return "Erro"
    
    # Função que calcula o inverso (1/x)
    def inverso(self):
        try:
            num = float(self.show)
            if num != 0:
                return str(1 / num)
            else:
                return "Div/0"
        except ValueError:
            return "Erro"
    
    # Função que calcula a porcentagem
    def porcentagem(self):
        try:
            result = float(self.show) / 100
            return str(result)
        except ValueError:
            return "Erro"
    
    # Função que arredonda o valor
    def arredondar(self):
        try:
            result = round(float(self.show), 2)
            return str(result)
        except ValueError:
            return "Erro"
