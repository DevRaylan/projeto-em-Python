import tkinter as tk

class Relatorio:
    def __init__(self, alunos):
        self.alunos = alunos

    def gerar_relatorio_gui(self, texto_widget, professor):
        if not professor:
            raise ValueError("O objeto professor não foi fornecido corretamente.")
        
        # Adicionando o nome do professor, disciplina, código da disciplina e ano no topo
        texto_widget.insert(tk.END, f"Professor: {professor.nome}\n")
        texto_widget.insert(tk.END, f"Disciplina: {professor.disciplina}\n")
        texto_widget.insert(tk.END, f"Código da Disciplina: {professor.codigo_disciplina}\n")
        texto_widget.insert(tk.END, f"Ano: {professor.ano}\n")
        texto_widget.insert(tk.END, "-"*50 + "\n")

        # Gerando o relatório para cada aluno
        for aluno in self.alunos:
            notas_formatadas = ', '.join([f"{nota:.2f}" for nota in aluno.notas])
            media_formatada = f"{aluno.calcular_media():.2f}"
            texto_widget.insert(tk.END, f"Aluno: {aluno.nome}\n")
            texto_widget.insert(tk.END, f"Notas: {notas_formatadas}\n")
            texto_widget.insert(tk.END, f"Média: {media_formatada}\n")
            texto_widget.insert(tk.END, f"Situação: {aluno.situacao()}\n")
            texto_widget.insert(tk.END, "-"*50 + "\n")
