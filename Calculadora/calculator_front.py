# -*- coding:utf-8 -*-
from tkinter import *
from calculator_back import Calculator

# Criando a aplicação
app = Tk()
app.resizable(0, 0)
app.title("Calculadora Python")

# Removendo a transparência
# Basta não incluir a linha app.attributes("-alpha", 0.95)

# Instanciando a classe da calculadora
calc = Calculator()

equation = StringVar()  # variável que vai mostrar o texto

# Display da calculadora com bordas arredondadas e fundo suave
display = Label(app, textvariable=equation, height=2, anchor="e", font=("Arial", 24), bg="#F0F0F0", padx=10, relief="flat", bd=0, highlightthickness=0)
equation.set("0")  # texto inicial no display
display.grid(row=0, columnspan=5, sticky="nsew", padx=10, pady=10)

# Função que adiciona o valor do botão pressionado ao display
def btnPress(num):
    calc.btnPress(num)
    equation.set(calc.show)

# Função que faz o cálculo da equação
def evaluate():
    result = calc.evaluate()
    equation.set(result)
    calc.show = ""

# Função que limpa o display
def clear():
    calc.clear()
    equation.set(calc.show)

# Função que calcula o fatorial
def fatorial():
    result = calc.fatorial()
    equation.set(result)
    calc.show = ""

# Função que calcula a raiz quadrada
def raiz():
    result = calc.raiz()
    equation.set(result)
    calc.show = ""

# Função que calcula o inverso (1/x)
def inverso():
    result = calc.inverso()
    equation.set(result)
    calc.show = ""

# Função que calcula a porcentagem
def porcentagem():
    result = calc.porcentagem()
    equation.set(result)
    calc.show = ""

# Função que arredonda o valor
def arredondar():
    result = calc.arredondar()
    equation.set(result)
    calc.show = ""

# Função para botões personalizados com bordas arredondadas e cores modernas
def create_button(text, row, column, width=5, height=2, bg_color="#5F9EA0"):
    return Button(app, text=text, command=lambda: btnPress(text) if text != "=" else evaluate(),
                  width=width, height=height, font=("Arial", 18), bg=bg_color, fg="white", 
                  borderwidth=0, relief="flat", activebackground="#3CB371", activeforeground="white", 
                  padx=20, pady=20, highlightthickness=0, bd=5, highlightbackground="#32CD32", highlightcolor="#32CD32",
                  border=6, # borda mais espessa
                  )

# Layout dos botões
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3), ('-', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('/', 2, 4),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x²', 3, 3), ('√', 3, 4),
    ('0', 4, 1), ('.', 4, 0), ('%', 4, 2), ('1/x', 4, 3), ('=', 4, 4),
    ('C', 5, 0), ('n!', 5, 1), ('(', 5, 2), (')', 5, 3), ('arredondar', 5, 4)
]

# Adicionando os botões ao layout
for (text, row, col) in buttons:
    bg_color = "#4CAF50" if text not in ["=", "C", "n!", "arredondar"] else "#FF6347"
    create_button(text, row, col, bg_color=bg_color).grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

# Ajustar o tamanho das colunas e linhas para que ocupem toda a área disponível
for i in range(5):
    app.grid_columnconfigure(i, weight=1)
    app.grid_rowconfigure(i, weight=1)

# Funções para os botões especiais
Button(app, text="C", command=clear, width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", relief="flat", borderwidth=0, activebackground="#FF4500").grid(row=5, column=0, padx=5, pady=5)
Button(app, text="n!", command=fatorial, width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", relief="flat", borderwidth=0, activebackground="#FF4500").grid(row=5, column=1, padx=5, pady=5)
Button(app, text="(", command=lambda: btnPress('('), width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", relief="flat", borderwidth=0, activebackground="#FF4500").grid(row=5, column=2, padx=5, pady=5)
Button(app, text=")", command=lambda: btnPress(')'), width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", relief="flat", borderwidth=0, activebackground="#FF4500").grid(row=5, column=3, padx=5, pady=5)
Button(app, text="arredondar", command=arredondar, width=5, height=2, font=("Arial", 18), bg="#FF6347", fg="white", relief="flat", borderwidth=0, activebackground="#FF4500").grid(row=5, column=4, padx=5, pady=5)

# Rodando a interface
app.mainloop()