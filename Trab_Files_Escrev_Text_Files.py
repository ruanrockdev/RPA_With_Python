# Criando arquivo com texto dentro

lines = ["readme", "How to write text files in Python"]
with open("readme.txt", "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")  # Colocando uma linha em cada intervalo ","
f.close()
print("-----------------------------------------------")
