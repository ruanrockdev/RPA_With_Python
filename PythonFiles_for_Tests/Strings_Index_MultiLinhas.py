# Multiplas linhas, muito usado pra comentários longos em várias linhas para documentação em Python

print('''Bom dia pessoal, 
Estamos escrevendo multiplas linhas,
usando as 3 aspas''')

# Indexando e fatiando uma String
# 0 é o primeiro e -1 é o ultimo
print("")
sFrase = "Hello world!"
print("Mostrando com Índice\n", sFrase[0: -1])  # ou
print("Mostrando com Índice\n", sFrase[: -1])

# IN e NOT IN, verifica se está ou não na string
# RETORNA UMA BOLEAN
print("")
sFrase2 = "Hello world!"
print("Hello" in sFrase2)
print("HELLO" in sFrase2)

sValida = "e" not in sFrase2
print(sValida)
