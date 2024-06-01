dogs = ['Spike', 'Duke', 'Rex', 'Skipper']
# usamos o len pra fazer o loop pela quantidade de itens na tabela igual aomation rs
for i in range(len(dogs)):
    # aqui eu mostro o i que é o numero do index da posicao do item e depois o item da lista nessa posicao
    # ou por str(i) no primeiro i
    print("Posição", i, "temos o cachorro:", dogs[i])

# forma alternativa de executar o range
for index, dog in enumerate(dogs):
    print(dog)
