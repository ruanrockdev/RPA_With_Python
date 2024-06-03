# Vamos converter xlsx in Json and more, lets do it ;)
import openpyxl

wb = openpyxl.load_workbook("products.xlsx")
sheet = wb["Sheet1"]

# Obtendo o total de linhas com dados para usar
nTotalLinhas = sheet.max_row

for row in sheet.iter_rows(min_row=1, max_row=nTotalLinhas, min_col=1, max_col=3, values_only=True):
    print(row)
