import pandas as pd

# Leitura da planilha Excel
df = pd.read_excel(
    'D:\TRABALHO E FACUL E CURSOS\CURSOS E TI PCs\CURSOS\RPA\PYTHON\Luiz Fernando Estivalet\RPA_With_Python\PythonFiles_for_Tests\Excel_PlanilhaExemplo.xlsx')

# Exemplo de mapeamento de colunas para variáveis
coluna1 = df['Data'].tolist()
coluna2 = df['Fruta'].tolist()
coluna3 = df['Valor'].tolist()

# Agora coluna1, coluna2, coluna3 são listas contendo os dados das respectivas colunas
print(coluna1)
print(coluna2)
print(coluna3)
