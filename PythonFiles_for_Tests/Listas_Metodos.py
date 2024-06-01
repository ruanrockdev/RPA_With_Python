'''
MÉTODOS de listas, porém, não alteram a estrutura da lista em sí e manipulam itens
INDEX()
APPEND()
INSERT()
POP()
REMOVE()
REVERSE()
SORT()
COUNT()
'''
livros = []

# INDEX mostra o index do item na lista
print("\n")
livros = ["JAVA", "JAVA", "C#", "SQL", "PYTHON"]
print(livros.index("SQL"))
print("-----------------------------------------------")
print("\n")

# APPEND acrescenta um item no final da lista
livros.append("C++")
print(livros)
print("-----------------------------------------------")
print(" ")

# INSERT - Acrescenta um item no index indicado da lista
livros.insert(0, "ANGULAR")
print(livros)
print("-----------------------------------------------")
print(" ")

# POP - Remove o ultimo item da lista ou usando um indice
livros.pop()
print(livros)
print("-----------------------------------------------")
print("\n")

# REMOVE - Remove um item da lista pelo Nome do item indicado
livros.remove("ANGULAR")
print(livros)
print("-----------------------------------------------")
print("\n")

# REVERSE - INVERTE a lista
livros.reverse()
print(livros)
print("-----------------------------------------------")
print("\n")

# SORT - ORDENAR a lista em ordem alfabética crescente
livros.sort()
print(livros)
print("-----------------------------------------------")
print("\n")

# COUNT - retorna o número o ocorrencias de um item na lista mas precisa ser posto em variavel
total = livros.count("JAVA")
print("Temos", total, "itens chamado:JAVA na lista")
print("-----------------------------------------------")
print("\n")

# l = ["  JOSÉ MIGUEL  "]
# print(l * 500)
