# Copiando dicionarios

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

# não podemos fazer: car2 = car pro que assim copiariamos somente a referencia

car2 = car.copy()
print("lista normal", car)
print("Lista pura copiada", car2)

car2["color"] = "black"
print("Com adição", car2)

# if "color" not in car:
#    car2["color"] = "black"

# setdefault só funciona caso a chave nao exista, se existir ele não fará nada
car.setdefault("color", "black")
print(car)

# Contando quantas ocorrencias de letras na frase
sFrase = "Estou aprendendo python RPA"
count = {}
for i in sFrase:
    count.setdefault(i, 0)
    count[i] = count[i] + 1

print(count)


# unindo dicionarios
UnicaoCars = {**car, **car2}
print("Listas Unidas", UnicaoCars)
