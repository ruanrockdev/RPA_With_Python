fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# nova lista com for na lista usando x mas só se o x for diferente de apple
# Usando condicional
print("Lista com fruits completa", fruits)
newlist = [x for x in fruits if x != "apple"]
print("Lista fruits sem o apple", newlist)

# Colocando itens em maiúsculo na lista (strings)
upperlist = [x.upper() for x in fruits]
print("Lista com nomes em maiusculo", upperlist)

# printando x no range de 10
listNumber = [x for x in range(10)]
print("lista com range 10", listNumber)

# condicionando o x com range e 20 onde o x tem que ser maior que 5
listcond = [x for x in range(20)if x > 5]
print("lista com range 20 e if > que 5", listcond)

# Essa linha mostra numeros de 1 a 100 (um em cada linha)
for i in range(1, 101):
    # com essa linha ele faz uma validação para pegar os numeros com raiz quadrada exata.
    if int(i**0.5) == i**0.5:
        print(i)

# Usando list comprehension
numeros = [i for i in range(1, 101) if int(i ** 0.5) == i ** 0.5]
print("Usando Comprehension", numeros)
