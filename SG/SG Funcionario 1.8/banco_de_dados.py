import sqlite3
import shutil
import os
from datetime import datetime
from tabulate import tabulate  # Importação corrigida

def conectar_banco():
    """Conectar ao banco de dados SQLite"""
    return sqlite3.connect('empresa.db')

def criar_tabela():
    """Cria a tabela de funcionários se ela não existir"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        salario REAL NOT NULL,
        tipo TEXT NOT NULL,
        departamento TEXT,
        linguagem_programacao TEXT
    )
    ''')
    conn.commit()
    conn.close()

def adicionar_funcionario(funcionario):
    """Adiciona um funcionário ao banco de dados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO funcionarios (nome, idade, salario, tipo, departamento, linguagem_programacao)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        funcionario.nome,
        funcionario.idade,
        funcionario.salario,
        funcionario.__class__.__name__,
        getattr(funcionario, 'departamento', None),
        getattr(funcionario, 'linguagem_programacao', None)
    ))
    conn.commit()
    conn.close()

def listar_funcionarios():
    """Lista todos os funcionários da empresa com dados estruturados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()

    if not funcionarios:
        return 'Nenhum funcionário registrado.'

    # Cabeçalho da tabela
    cabecalho = ['ID', 'Nome', 'Idade', 'Salário', 'Tipo', 'Departamento', 'Linguagem']

    # Dados dos funcionários em formato tabular
    dados = [
        [
            funcionario[0],  # ID
            funcionario[1],  # Nome
            funcionario[2],  # Idade
            f'R${funcionario[3]:.2f}',  # Salário formatado
            funcionario[4],  # Tipo (ex: Funcionário, Gerente, Desenvolvedor)
            funcionario[5] if funcionario[5] else 'N/A',  # Departamento (caso exista)
            funcionario[6] if funcionario[6] else 'N/A'  # Linguagem (caso exista)
        ]
        for funcionario in funcionarios
    ]

    # Exibindo os dados na tabela
    tabela = tabulate(dados, headers=cabecalho, tablefmt='pretty')
    conn.close()
    return tabela

def buscar_funcionario(nome=None, id_funcionario=None):
    """Busca funcionário por nome ou ID"""
    conn = conectar_banco()
    cursor = conn.cursor()
    
    if nome:
        cursor.execute('SELECT * FROM funcionarios WHERE nome LIKE ?', (f'%{nome}%',))
    elif id_funcionario:
        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id_funcionario,))
    else:
        return 'Informe nome ou ID para busca.'
    
    funcionario = cursor.fetchone()
    conn.close()
    
    if funcionario:
        return f'ID: {funcionario[0]}, Nome: {funcionario[1]}, Idade: {funcionario[2]}, ' \
               f'Salário: R${funcionario[3]:.2f}, Tipo: {funcionario[4]}, ' \
               f'Departamento: {funcionario[5] if funcionario[5] else "N/A"}, ' \
               f'Linguagem: {funcionario[6] if funcionario[6] else "N/A"}'
    return 'Funcionário não encontrado.'

def excluir_funcionario(nome):
    """Exclui um funcionário pelo nome"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE nome LIKE ?', (f'%{nome}%',))
    conn.commit()
    conn.close()
    return f'Funcionário {nome} removido com sucesso.' if cursor.rowcount > 0 else 'Funcionário não encontrado.'

def editar_funcionario(nome, idade=None, salario=None, departamento=None, linguagem_programacao=None):
    """Edita dados de um funcionário"""
    conn = conectar_banco()
    cursor = conn.cursor()

    if idade:
        cursor.execute('UPDATE funcionarios SET idade = ? WHERE nome LIKE ?', (idade, nome))
    if salario:
        cursor.execute('UPDATE funcionarios SET salario = ? WHERE nome LIKE ?', (salario, nome))
    if departamento:
        cursor.execute('UPDATE funcionarios SET departamento = ? WHERE nome LIKE ?', (departamento, nome))
    if linguagem_programacao:
        cursor.execute('UPDATE funcionarios SET linguagem_programacao = ? WHERE nome LIKE ?', (linguagem_programacao, nome))
    
    conn.commit()
    conn.close()
    return f'Funcionário {nome} atualizado com sucesso!'

# Funções de Backup

def backup_dados():
    """Cria um backup do banco de dados atual."""
    try:
        # Caminho atual do banco de dados
        db_path = 'empresa.db'

        # Cria um nome de backup com base na data e hora
        backup_name = f"empresa_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"

        # Copia o banco de dados para o arquivo de backup
        shutil.copy(db_path, backup_name)
        print(f"Backup criado com sucesso! O arquivo de backup é: {backup_name}")
    except FileNotFoundError:
        print("Erro: O banco de dados não foi encontrado!")
    except Exception as e:
        print(f"Erro ao criar o backup: {e}")

def listar_backups():
    """Lista os arquivos de backup disponíveis no diretório."""
    backup_files = [f for f in os.listdir() if f.startswith('empresa_backup_') and f.endswith('.db')]
    
    if not backup_files:
        print("Nenhum backup encontrado.")
        return []
    
    print("Backups disponíveis:")
    for i, backup in enumerate(backup_files, 1):
        print(f"{i}. {backup}")
    
    return backup_files

def recuperar_backup():
    """Permite que o usuário recupere um backup a partir de uma lista."""
    backups = listar_backups()

    if not backups:
        return

    try:
        # Solicita ao usuário escolher qual backup deseja restaurar
        escolha = int(input(f"Escolha o número do backup que deseja restaurar (1-{len(backups)}): "))

        if 1 <= escolha <= len(backups):
            backup_selecionado = backups[escolha - 1]
            # Substitui o banco de dados atual pelo backup selecionado
            shutil.copy(backup_selecionado, 'empresa.db')
            print(f"Backup {backup_selecionado} restaurado com sucesso!")
        else:
            print("Escolha inválida.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
    except Exception as e:
        print(f"Erro ao restaurar o backup: {e}")