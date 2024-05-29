# Lendo arquivos com Python

# Estou lendo apenas o arquivo por que ele está na mesma pasta que estou trabalhando
# Passamos o encoding para aceitar os acentos
with open("soneto.txt", encoding="utf8") as f:
    contents = f.read()
    print(contents)

# Vamos contar as linhas usando um contador
lines = []
with open("soneto.txt", encoding="utf8") as f:
    lines = f.readlines()

# count = 0
# for line in lines:
#     count += 1
#     print(f"line {count}: {line}")

with open("soneto.txt", encoding="utf8") as f:
    line = f.readline()
    while line:  # Aqui temos um while enquanto tiver linha pra ler no arquivo
        print(line)
        line = f.readline()
