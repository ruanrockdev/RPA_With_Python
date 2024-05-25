# random.choice() nos mostra um item aleatório da lista
# random.shuffle() muda de maneira aleatório a ordem dos itens na lista
import random

dogs = ['Spike', 'Duke', 'Rex', 'Skipper']

# print(random.choice(dogs))
random.shuffle(dogs)
print(dogs)
