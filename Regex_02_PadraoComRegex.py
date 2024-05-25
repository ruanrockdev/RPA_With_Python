# Encontrando padrão Com Regex (DD) XXXXX-XXXX
import re

# Método Compile com search
numero_telefone = re.compile(r'\d\d\d\d\d-\d\d\d\d')
result = numero_telefone.search('Meu número é 87657-1029. Ligar Após as 19h.')
print('Telefone encontrado: ' + result.group())

numero_telefone2 = re.compile(r'\d{5}-\d{4}')
result2 = numero_telefone2.search('Me ligue no número 12345-1234')

# Boa Pra
if result2:
    print('Telefone encontrado: ' + result2.group())
else:
    print("Telefone não encontrado")
