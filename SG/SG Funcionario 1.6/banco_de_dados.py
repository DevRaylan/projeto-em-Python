import sqlite3
from tabulate import tabulate  # Para exibir os dados de forma estruturada

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
        linguagem_programacao TEXT,
        funcao_assistencial TEXT
    )
    ''')
    conn.commit()
    conn.close()

def adicionar_funcionario(funcionario):
    """Adiciona um funcionário ao banco de dados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO funcionarios (nome, idade, salario, tipo, departamento, linguagem_programacao, funcao_assistencial)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        funcionario.nome,
        funcionario.idade,
        funcionario.salario,
        funcionario.__class__.__name__,
        getattr(funcionario, 'departamento', None),
        getattr(funcionario, 'linguagem_programacao', None),
        getattr(funcionario, 'funcao_assistencial', None)
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

    cabecalho = ['ID', 'Nome', 'Idade', 'Salário', 'Tipo', 'Departamento', 'Linguagem', 'Função Assistencial']
    dados = [
        [
            funcionario[0],  # ID
            funcionario[1],  # Nome
            funcionario[2],  # Idade
            f'R${funcionario[3]:.2f}',  # Salário formatado
            funcionario[4],  # Tipo
            funcionario[5] if len(funcionario) > 5 and funcionario[5] else 'N/A',  # Departamento
            funcionario[6] if len(funcionario) > 6 and funcionario[6] else 'N/A',  # Linguagem
            funcionario[7] if len(funcionario) > 7 and funcionario[7] else 'N/A'  # Função Assistencial
        ]
        for funcionario in funcionarios
    ]
    tabela = tabulate(dados, headers=cabecalho, tablefmt='pretty')
    conn.close()
    return tabela

    """Lista todos os funcionários da empresa com dados estruturados"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM funcionarios')
    funcionarios = cursor.fetchall()

    if not funcionarios:
        return 'Nenhum funcionário registrado.'

    cabecalho = ['ID', 'Nome', 'Idade', 'Salário', 'Tipo', 'Departamento', 'Linguagem', 'Função Assistencial']
    dados = [
        [
            funcionario[0],  # ID
            funcionario[1],  # Nome
            funcionario[2],  # Idade
            f'R${funcionario[3]:.2f}',  # Salário formatado
            funcionario[4],  # Tipo
            funcionario[5] if funcionario[5] else 'N/A',  # Departamento
            funcionario[6] if funcionario[6] else 'N/A',  # Linguagem
            funcionario[7] if funcionario[7] else 'N/A'  # Função Assistencial
        ]
        for funcionario in funcionarios
    ]
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
               f'Linguagem: {funcionario[6] if funcionario[6] else "N/A"}, ' \
               f'Função Assistencial: {funcionario[7] if funcionario[7] else "N/A"}'
    return 'Funcionário não encontrado.'

def excluir_funcionario(nome):
    """Exclui um funcionário pelo nome"""
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM funcionarios WHERE nome LIKE ?', (f'%{nome}%',))
    conn.commit()
    conn.close()
    return f'Funcionário {nome} removido com sucesso.' if cursor.rowcount > 0 else 'Funcionário não encontrado.'

def editar_funcionario(nome, idade=None, salario=None, departamento=None, linguagem_programacao=None, funcao_assistencial=None):
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
    if funcao_assistencial:
        cursor.execute('UPDATE funcionarios SET funcao_assistencial = ? WHERE nome LIKE ?', (funcao_assistencial, nome))
    
    conn.commit()
    conn.close()
    return f'Funcionário {nome} atualizado com sucesso.'
