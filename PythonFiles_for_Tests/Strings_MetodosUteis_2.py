# Métodos úteis parte 2
import pyperclip

# Método strip() > retorna uma string sem espaços no inicio e fim
sNome = "   RPA   "
print("Com espaço inicio e fim|" + sNome + "|")
print("Sem espaço inicio e fim|" + sNome.strip() + "|")

# o lstrip() remove espaço do lado esquerdo da string
# 0 rstrip() remove espaço do lado direito da string

# depois de instalar pyperclip que pode enviar e receber textos da área de transferencia, é muito usado em automacao pra enviar email e escrever textos.abs

# pyperclip.copy("Hello, World")  # CTRL + C na string
# print(pyperclip.paste())  # CTRL + V da área de transferencia

# Item 1
# Item 2
# Item 3
# Item 4
# Item 5
# Item 6
# Item 7
# Item 8

# * Item 1
# * Item 2
# * Item 3
# * Item 4
# * Item 5
# * Item 6
# * Item 7
# * Item 8

# text = pyperclip.paste()
# lines = text.split("\n")
# for i in range(len(lines)):
#     lines[i] = "* " + lines[i]

# text = "\n".join(lines)
# pyperclip.copy(text)


# ---------------------------------------------------
# Copia um texto para o clipboard
pyperclip.copy("Este texto está agora no clipboard.")

# Cola o texto do clipboard
texto_do_clipboard = pyperclip.paste()
print("Texto colado do clipboard:", texto_do_clipboard)
# --------------------------------------------------

# rjust e ljust soma espaços a string
print("TEXTO".rjust(10))
print("TEXTO".rjust(10, "*"))  # troca o espaço por * ou oque quiser
print("TEXTO".ljust(10, "*"))
print("TEXTO".center(30, "_"))  # centraliza a spring

# --------------------------------------------------------------------------------
compras = {"Refrigerantes": 4, "Laranjas": 12, "maças": 15, "bananas": 30}


def imprimir(dic_items, largura_col_esq, largura_col_dir):
    print("LISTA DE COMPRAS".center(largura_col_esq + largura_col_dir, "-"))
    for k, v in dic_items.items():
        print(k.ljust(largura_col_esq, ".") + str(v).rjust(largura_col_dir))


imprimir(compras, 50, 3)
