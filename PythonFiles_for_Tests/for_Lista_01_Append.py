lista = []
i = 1
while True:
    item = input("Digite nome do Item para adicionar (ou nada para parar): ")
    if item != "":
        lista.append(item)        
    else:
        break
        
nCounter = len(lista)
print("Ual, sua lista tem:", nCounter, "itens")

for i in range(nCounter):
    print(lista[i])
