# Encontrando padrão Com Regex (DD) XXXXX-XXXX
import re

# Método Compile com search
numero_telefone = re.compile(r'\d\d\d\d\d-\d\d\d\d')
result = numero_telefone.search('Meu número é 87657-1029. Ligar Após as 19h.')
print('Telefone encontrado: ' + result.group())

numero_telefone2 = re.compile(r'\d{5}-\d{4}')
result2 = numero_telefone2.search('Me ligue no número 12345-1234')

# Boa Pratica com validação em caso de erro
if result2:
    print('Telefone encontrado: ' + result2.group())
else:
    print("Telefone não encontrado")

# Mapeando telefone com DDD
numero_telefone3 = re.compile(r'\(\d{2}\)\d{5}-\d{4}')
result3 = numero_telefone3.search(
    "O Numero de telefone com DDD é esse (55)12345-1234")
if result3:
    print("Telefone com DDD é: " + result3.group())
else:
    print("Telefone não encontrado")

# Regex é um padrão complicado a princípio mas depois é a melhor coisa que tem
