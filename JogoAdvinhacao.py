# Jogo da advinhação

import random
secretNumber = random.randint(1, 20)
print("Estou pensando em um número de 1 a 20, Você tem 7 chances")

for tentativas in range(1, 8):  # Laço de repetição que vai de 1 a 8 (executa 7 vezes)
    print("Tente advinhar o número")
    chute = input()

   # Validação para pedir apenas números
    try:
        chute = int(chute)
    except ValueError:
        print("Insira apenas Números")
        continue

    if chute < secretNumber:
        print("Sua tentativa foi BAIXA")
    elif chute > secretNumber:
        print("Sua tentativa foi ALTA")
    else:
        break

if chute == secretNumber:
    print("Muito Bem! Você Acertou o número em " +
          str(tentativas) + " tentativas")
else:
    print("Que pena!, você não conseguiu acertar o número que era: " + str(secretNumber))
