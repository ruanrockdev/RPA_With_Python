# import pandas as pd

# # Leitura da planilha Excel
# df = pd.read_excel(
#     'D:\TRABALHO E FACUL E CURSOS\CURSOS E TI PCs\CURSOS\RPA\PYTHON\Luiz Fernando Estivalet\RPA_With_Python\PythonFiles_for_Tests\Excel_PlanilhaExemplo.xlsx')

# # Exemplo de mapeamento de colunas para variáveis
# coluna1 = df['Data'].tolist()
# coluna2 = df['Fruta'].tolist()
# coluna3 = df['Valor'].tolist()

# # Agora coluna1, coluna2, coluna3 são listas contendo os dados das respectivas colunas
# print(coluna1)
# print(coluna2)
# print(coluna3)

#
import pandas as pd


PlanilhaDados = "D:\TRABALHO E FACUL E CURSOS\CURSOS E TI PCs\CURSOS\RPA\PYTHON\Luiz Fernando Estivalet\RPA_With_Python\PythonFiles_for_Tests\dados.xlsx"
# Leitura da planilha Excel
df = pd.read_excel(PlanilhaDados)

# Lista para armazenar os dados
dados = []

# Percorrendo linha por linha do DataFrame
for index, row in df.iterrows():
    # Armazenando os valores em um dicionário
    registro = {
        'nome': row['Nome'],
        'idade': row['Idade'],
        'cidade': row['Cidade']
    }

    # Adicionando o dicionário à lista
    dados.append(registro)

# Exemplo de uso dos dados armazenados
for registro in dados:
    # print(
    #     f"Nome: {registro['nome']}, Idade: {registro['idade']}, Cidade: {registro['cidade']}")
    print(registro['nome'], registro['idade'], registro['cidade'])
