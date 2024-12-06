import tkinter as tk
from tkinter import messagebox, filedialog
from aluno import Aluno
from professor import Professor
from relatorio import Relatorio

class SistemaAcademicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Análise Acadêmica")

        # Variáveis
        self.alunos = []
        self.professores = []
        self.caminho_arquivo = None  # Inicialmente, o caminho do arquivo é None

        # Frame para adicionar professor
        self.frame_professor = tk.LabelFrame(self.root, text="Adicionar Professor", padx=10, pady=10)
        self.frame_professor.grid(row=0, column=0, padx=10, pady=10)

        self.label_nome_professor = tk.Label(self.frame_professor, text="Nome do Professor:")
        self.label_nome_professor.grid(row=0, column=0)

        self.entry_nome_professor = tk.Entry(self.frame_professor)
        self.entry_nome_professor.grid(row=0, column=1)

        self.label_disciplina = tk.Label(self.frame_professor, text="Disciplina:")
        self.label_disciplina.grid(row=1, column=0)

        self.entry_disciplina = tk.Entry(self.frame_professor)
        self.entry_disciplina.grid(row=1, column=1)

        self.label_codigo_disciplina = tk.Label(self.frame_professor, text="Código da Disciplina:")
        self.label_codigo_disciplina.grid(row=2, column=0)

        self.entry_codigo_disciplina = tk.Entry(self.frame_professor)
        self.entry_codigo_disciplina.grid(row=2, column=1)

        self.label_ano = tk.Label(self.frame_professor, text="Ano:")
        self.label_ano.grid(row=3, column=0)

        self.entry_ano = tk.Entry(self.frame_professor)
        self.entry_ano.grid(row=3, column=1)

        self.botao_adicionar_professor = tk.Button(self.frame_professor, text="Adicionar Professor", command=self.adicionar_professor)
        self.botao_adicionar_professor.grid(row=4, columnspan=2)

        # Frame para adicionar aluno
        self.frame_aluno = tk.LabelFrame(self.root, text="Adicionar Aluno", padx=10, pady=10)
        self.frame_aluno.grid(row=0, column=1, padx=10, pady=10)

        self.label_nome_aluno = tk.Label(self.frame_aluno, text="Nome do Aluno:")
        self.label_nome_aluno.grid(row=0, column=0)

        self.entry_nome_aluno = tk.Entry(self.frame_aluno)
        self.entry_nome_aluno.grid(row=0, column=1)

        self.label_notas = tk.Label(self.frame_aluno, text="Notas (separadas por vírgula ','):")
        self.label_notas.grid(row=1, column=0)

        self.entry_notas = tk.Entry(self.frame_aluno)
        self.entry_notas.grid(row=1, column=1)

        self.botao_adicionar_aluno = tk.Button(self.frame_aluno, text="Adicionar Aluno", command=self.adicionar_aluno)
        self.botao_adicionar_aluno.grid(row=2, columnspan=2)

        # Botão para gerar relatório
        self.botao_gerar_relatorio = tk.Button(self.root, text="Gerar Relatório", command=self.gerar_relatorio)
        self.botao_gerar_relatorio.grid(row=1, column=0, columnspan=2, pady=10)

        # Área para exibir o relatório
        self.texto_relatorio = tk.Text(self.root, height=15, width=50)
        self.texto_relatorio.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def adicionar_professor(self):
        nome = self.entry_nome_professor.get()
        disciplina = self.entry_disciplina.get()
        codigo_disciplina = self.entry_codigo_disciplina.get()
        ano = self.entry_ano.get()

        if not nome or not disciplina or not codigo_disciplina or not ano:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
            return

        # Convertendo o ano para um número inteiro, se possível
        try:
            ano = int(ano)
        except ValueError:
            messagebox.showwarning("Ano inválido", "O campo 'Ano' precisa ser um número válido!")
            return

        professor = Professor(nome, disciplina, codigo_disciplina, ano)
        self.professores.append(professor)

        # Pedir ao usuário para escolher onde salvar o arquivo ao adicionar o primeiro professor
        if not self.caminho_arquivo:
            caminho = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
            if not caminho:
                messagebox.showwarning("Caminho não escolhido", "Você precisa escolher um local para salvar o arquivo!")
                return
            self.caminho_arquivo = caminho

        # Limpar os campos
        self.entry_nome_professor.delete(0, tk.END)
        self.entry_disciplina.delete(0, tk.END)
        self.entry_codigo_disciplina.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)

        messagebox.showinfo("Professor Adicionado", f"Professor {nome} adicionado com sucesso!")

    def adicionar_aluno(self):
        nome = self.entry_nome_aluno.get()
        notas_str = self.entry_notas.get()

        if not nome or not notas_str:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos!")
            return

        try:
            # Alteração: agora as notas são separadas por vírgula
            notas = [float(nota.strip()) for nota in notas_str.split(",")]
        except ValueError:
            messagebox.showwarning("Notas inválidas", "As notas precisam ser números válidos!")
            return

        # Assumimos que o aluno será adicionado ao último professor cadastrado
        if not self.professores:
            messagebox.showwarning("Erro", "Nenhum professor cadastrado!")
            return

        professor = self.professores[-1]
        ano = professor.ano  # Pega o ano do último professor cadastrado
        aluno = Aluno(nome, professor.disciplina, professor.codigo_disciplina, notas, ano)
        self.alunos.append(aluno)

        # Atualizar o arquivo e exibir na tela
        self.salvar_dados()
        self.atualizar_relatorio()

        # Limpar os campos
        self.entry_nome_aluno.delete(0, tk.END)
        self.entry_notas.delete(0, tk.END)

        messagebox.showinfo("Aluno Adicionado", f"Aluno {nome} adicionado com sucesso!")

    def gerar_relatorio(self):
        if not self.alunos or not self.professores:
            messagebox.showwarning("Dados faltando", "Não há alunos ou professores para gerar o relatório!")
            return

        professor = self.professores[-1]
        relatorio = Relatorio(self.alunos)
        self.texto_relatorio.delete(1.0, tk.END)  # Limpar a área de texto antes de gerar o novo relatório
        relatorio.gerar_relatorio_gui(self.texto_relatorio, professor)

    def salvar_dados(self):
        try:
            with open(self.caminho_arquivo, "w") as f:
                # Salvar informações dos professores
                for professor in self.professores:
                    f.write(f"Professor: {professor.nome}, Disciplina: {professor.disciplina}, Código: {professor.codigo_disciplina}, Ano: {professor.ano}\n")
                
                f.write("\n")  # Linha em branco separando professores de alunos
                
                # Salvar informações dos alunos
                for aluno in self.alunos:
                    f.write(f"Aluno: {aluno.nome}, Notas: {', '.join([f'{nota:.2f}' for nota in aluno.notas])}, Média: {aluno.calcular_media():.2f}, Situação: {aluno.situacao()}\n")
            messagebox.showinfo("Sucesso", f"Dados salvos em {self.caminho_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro ao salvar", f"Erro ao salvar arquivo: {e}")

    def atualizar_relatorio(self):
        # Atualiza a área de texto do relatório com os dados mais recentes
        if self.professores:
            professor = self.professores[-1]
            relatorio = Relatorio(self.alunos)
            self.texto_relatorio.delete(1.0, tk.END)  # Limpar a área de texto
            relatorio.gerar_relatorio_gui(self.texto_relatorio, professor)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAcademicoApp(root)
    root.mainloop()
