# Susbstituir variaveis no meio de strings deixando mais facil

name = "Ruan"
age = 42

# vamos converter o numero para string para mostrar ele na frase concatenando
# modo trabalhoso
print("Hello, my name is " + name + ". I am " + str(age) + " years old.")

print("")
# podemos usar virgula que deixa mais facil
print("Hello, my name is", name, ".", "I am", age, "years old.")

# Mais fácil ainda
print("")
print("Hello, my name is  %s. I am %s years old" % (name, age))

# no Python 3.6+ foi introduzido o F e fica mais fácil ainda e basta colocar CHAVES {VARIAVEL} e inclusive consegue fazer calculos com variavels numéricas

print("")
print(
    f"Hello, my name is {name}. I am {age} years old, and next year i will be {age + 1}")
