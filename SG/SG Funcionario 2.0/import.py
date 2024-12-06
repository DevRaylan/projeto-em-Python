import pandas as pd

# Teste de leitura de arquivo Excel
try:
    df = pd.read_excel("funcionarios.xlsx")
    print(df.head())  # Exibe as primeiras linhas do arquivo
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
