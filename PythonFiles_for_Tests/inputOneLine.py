import datetime

sNome = input("Qual é o seu nome? ")
nAnoNascimento = int(input("Em qual ano você nasceu? "))

nAno_Atual = datetime.datetime.now().year

nIdade = nAno_Atual - nAnoNascimento

if nIdade >= 30:
    sComentario = "Tá começando a ficar velho hein!"
elif nIdade >= 50:
    sComentario = "Cacete, tá ficando meio velho!"
else:
    sComentario = "Você ainda está novo!"

print("Olá", sNome, "você tem", nIdade, "Anos.", sComentario)