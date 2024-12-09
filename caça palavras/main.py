# main.py
import tkinter as tk
from back import criar_grade  # Importando a função do backend

# Função para exibir a grade
def exibir_grade():
    grade = criar_grade()
    for i in range(len(grade)):
        for j in range(len(grade[i])):
            label = tk.Label(root, text=grade[i][j], width=3, height=2, relief="solid", font=("Helvetica", 12))
            label.grid(row=i + 1, column=j)  # Ajustando a posição da grade para abaixo do botão
            labels[i][j] = label

# Criando a janela principal
root = tk.Tk()
root.title("Jogo de Caça-Palavras")

# Matriz para armazenar as labels
labels = [[None for _ in range(10)] for _ in range(10)]

# Botão para iniciar o jogo
botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=exibir_grade)
botao_iniciar.grid(row=0, column=0, columnspan=10)

# Iniciar o loop principal da interface
root.mainloop()
