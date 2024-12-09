# back.py
import random

def criar_grade():
    palavras = ["python", "javascript", "html", "css", "java", "ruby", "csharp"]
    tamanho_grade = 10  # Tamanho da grade
    grade = [['' for _ in range(tamanho_grade)] for _ in range(tamanho_grade)]
    
    # Adicionar palavras na grade de forma aleatória
    for palavra in palavras:
        direcao = random.choice(["horizontal", "vertical"])
        palavra_adicionada = False
        while not palavra_adicionada:
            if direcao == "horizontal":
                linha = random.randint(0, tamanho_grade - 1)
                coluna = random.randint(0, tamanho_grade - len(palavra))
                if all(grade[linha][coluna + i] == '' for i in range(len(palavra))):
                    for i in range(len(palavra)):
                        grade[linha][coluna + i] = palavra[i]
                    palavra_adicionada = True
            else:  # vertical
                linha = random.randint(0, tamanho_grade - len(palavra))
                coluna = random.randint(0, tamanho_grade - 1)
                if all(grade[linha + i][coluna] == '' for i in range(len(palavra))):
                    for i in range(len(palavra)):
                        grade[linha + i][coluna] = palavra[i]
                    palavra_adicionada = True

    # Preencher as células restantes com letras aleatórias
    for i in range(tamanho_grade):
        for j in range(tamanho_grade):
            if grade[i][j] == '':
                grade[i][j] = random.choice("abcdefghijklmnopqrstuvwxyz")
    
    return grade
