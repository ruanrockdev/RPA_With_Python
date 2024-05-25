# Métodos: items(), keys() e values()

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key, value in car.items():
    print(f"Key = {key}, value = {value}")

# Se a chave nao existir vai retornar None
print(car.get("model", "Key not found"))

# o keys é um método
for key in car.keys():  # no lugar de key poderia ser i ou qualquer
    print(f'Key={key}, value={car[key]}')

# método com print mais conhecido
for i in car.keys():
    print("Key =", i, "Value =", car[i])

# obter uma lista só com valores, usando método values
notas = {"Matemática": 8.3, "Português": 6.4,
         "História": 7.1, "Inglês": 9, "Ciências": 6}

for nota in notas.values():  # no lugar de nota poderia ser qualquer
    print(f"Valor: {nota}")

for i in notas.values():
    print("Valor:", i)

# Método para validar se determinada chave existe
if "Ciências" in notas:
    print("Matéria é:", notas["Ciências"])
else:
    print("A Matéria não existe no array das notas")

# Método para validar se determinado valor existe
if 6 in notas.values():
    print("Temos esse valor")
else:
    print("não temos esse valor")
