import openpyxl

wb = openpyxl.load_workbook("Append.xlsx")
sheet = wb.active
Sheet.insert_cols(1)  # Inserindo uma coluna
sheet.delete_cols(1)  # Deletando uma coluna
wb.save("Append.xlsx")
