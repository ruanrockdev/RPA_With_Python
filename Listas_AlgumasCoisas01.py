lista1 = ["maça", "pera", "uva", "laranja"]
lista2 = [1, 2, 3, 4, 5, 6, 76, lista1]

# Colocar -1 pega o ultimo elemento, -2 o antepenultimo e assim vai
print(lista1[-1])
print("-----------------------------------------------")

# Podemos mostrar itens de uma lista dentro de outra
print(lista2[-1])
print("-----------------------------------------------")

# também podemos mostrar os itens indexados de uma lista dentro de outra lista
print(lista2[-1][0])
print("-----------------------------------------------")

# Mostrando intervalo de elementos, vai mostrar do 0 até o indice 5 sempre termina um numero antes
print(lista2[0:5])
print("-----------------------------------------------")

# Também posso iniciar de um indice diferente do 0 ou sem nenhum
print(lista2[2:-1])
print("-----------------------------------------------")

# Mostar o tamanho de uma lista
print("Lista2 tem:", len(lista2), " elementos",
      "lista 1 tem:", len(lista1), " Elementos")
print("-----------------------------------------------")

# Alterando valores:
print("Antes de alterar o indice 0")
print(lista2)
lista2[0] = "Zero"
print("Depois de alterar o indice 0")
print(lista2)
print("-----------------------------------------------")

# Alterando valores de uma lista como sublista
print("Antes de alterar o indice 0")
print(lista2)
lista2[7][1] = "Alterado"
print("Depois de alterar o indice 0")
print(lista2)
print("-----------------------------------------------")

# Verificar se um item está em uma lista  usando o in
existe = 'dog' in lista1  # Atribui a uma variavel e retorna uma boliana
print(existe)  # printou false por que esse item não está na lista
print("-----------------------------------------------")

# retornar mínimo ou máximo valor de uma lista (min, max) e a soma dos valores (sum)
# Com Strings ele compara o tamanho da string (min, max), porém somar retorna ERRO
listaNumeros = [3, 5, 2, 8, 10, 4, 6, 7.5]
listaNomes = ["maça", "pera", "uva", "laranja"]
print(min(listaNumeros))
print(max(listaNumeros))
print(sum(listaNumeros))
print(min(listaNomes))
print(max(listaNomes))
# print(sum(listaNomes)) SOMAR RETORNA ERRO, não podemos somar strings só comparar
print("-----------------------------------------------")
