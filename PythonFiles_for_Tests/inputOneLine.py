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

# Brincando com print F colocando \n pra pular a linha
print(f"Olá {sNome}.\nVocê tem {nIdade} Anos.\n{sComentario}")
