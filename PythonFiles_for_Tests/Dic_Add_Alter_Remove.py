# Adicionando, alterando ou removendo chaves e valores

car = {"brand": "Ford", "model": "Mustang", "year": 1964}
print("Lista inicial", car)

# Adicionando valor e chave
car["color"] = "red"
print("Lista com adição", car)

# alterando com update, ele tanto cria quanto atualiza
car.update({"color": "black"})
print("Lista com UPDATE", car)

# Excluir elementos do Dicionário, 1
del car["year"]
print("Lista com remoção 1", car)

# Excluir valor do Dicionário, 1
# car.pop("model")
sItemRemovido = car.pop("model")
print("Lista com remoção 2", car)
print("Item removido:", sItemRemovido)
