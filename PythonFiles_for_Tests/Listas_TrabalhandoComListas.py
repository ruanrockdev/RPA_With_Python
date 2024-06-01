lListaNomes = []

while True:
    print("Digite um nome para incluir na lista ou apenas ENTER para encerrar: ")
    item = input()
    if item == "":
        break
    else:
        lListaNomes.append(item)

print("Sua lista tem", len(lListaNomes), "Itens\n")
print("Os Itens da lista em uma linha só são: ")
print(lListaNomes)
print("\n")
print("Os ites da sua lista com 1 item em cada linha é: ")
for i in lListaNomes:
    print(i)
