# Métodos úteis parte 1

# Upper e Lower
# Repare que a conversão é feita usando outra variavel e assim mantem a original
s = "Bem vindo ao curso de python com rpa"
s1 = s.upper()
print("Método UPPER:", s1)

print("")
s2 = s.lower()
print("Método LOWER:", s2)

# Validação de entrada de dados usando lower, pede pra digitar algo mas tanto maiusculo quanto minusculo vai ser convertido pra minusculo e se adaptar a validação mas mantendo o valor original
print("")
# sInput = ""
# while sInput.lower() != "fim":
#     print("Digite fim para terminar")
#     sInput = input()

# Método is lower is upper que retorna true ou false
print("")
m = "CAIXA ALTA"
print(m.islower())
print(m.isupper())

# Métodos de verificação

# isalpha = retorna true se todos os caracteres forem letras e não é vazia
print("")
print("python".isalpha())
print("python123".isalpha())

# isalnum = retorna true se tiver letras e numeros e não for vazia
print("")
print("python".isalnum())
print("python123".isalnum())
print("123546".isalnum())

# isdecimal = retorna true se a string estiver apenas com números e não for vazia
print("")
print("123".isdecimal())
print("python123".isdecimal())

# isspace = retorna true se a string tiver apenas espaços
print("")
print(" ".isspace())
print("python123".isspace())

# istitle = retorna true se a string for camel case (Ruan Certo)
print("")
print("ruan rock".istitle())
print("Ruan Rock".istitle())

# Validação para usar apenas numeros
# while True:
#     print("Entre sua idade")
#     age = input()
#     if age.isdecimal():  # validação se está usando apenas numeros
#         print(f"OK, vc tem {age} anos")
#         break
#     else:
#         print("Digite apenas Números")


# validação de senhas com apenas letras e numeros

# while True:
# print("Digite sua senha")
# PassWord = input()
# if PassWord.isalnum():
#     print("Senha salva com sucesso!")
#     break
# else:
#     print("Digite apenas numeros e letras")

# Metodo startswith COMECA COM
print("")
print("ruan rock".startswith("ruan"))
print("ruan rock".startswith("rock"))

# Metodo endswith TERMINA COM
print("")
print("ruan rock".endswith("ruan"))
print("ruan rock".endswith("rock"))

# Metodo JOIN, unindo uma string entre strings
print("")
print(", ".join(["cats", "rats", "bats"]))

print("")
print("_,_".join(["cats", "rats", "bats"]))

# Metodo SPLIT, DIVIDE strings em uma lista, por padrão ele divide ao encontrar espaço, TAB ou caracter de nova linha for encontrado ou podemos passar um delimitador para o método, o delimitador é removido
print("")
print("Meu nome, é Ruan".split())  # Sem delimitador (usando espaço padrão)
print("Meu nome, é Ruan".split(","))  # Com Delimitador

# Multilinhas
print("")
sTexto = '''Bom dia pessoal,
Estamos escrevendo multiplas linhas,
usando as 3 aspas'''
print(sTexto.split("\n"))  # Com Delimitador NOVA LINHA
