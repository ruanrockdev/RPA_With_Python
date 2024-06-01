import openpyxl

# Abrindo a planilha
wb = openpyxl.load_workbook("Excel_PlanilhaExemplo.xlsx")
print("Mostrando o Tipo do arquivo", type(wb))
print("Mostrando o nome das abas da planilha", wb.sheetnames)

sheet = wb["Sheet1"]
print(sheet)

# Retorna qual aba está ativa no momento
activeSheet = wb.active
print(activeSheet)

# Retorna a quantidade de linhas com dados
print("Quantidade de Linhas:", sheet.max_row)

# Retorna a quantidade de colunas com dados
print("Quantidade de Colunas:", sheet.max_column)
