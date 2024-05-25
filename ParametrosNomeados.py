def calcula_imc(peso, altura):
    print(peso / altura ** 2)
    
peso = float(input("Vamos calcular o seu índice de massa corporal, Digite o seu Peso: ")) #uma linha apenas

print("Qual é a sua altura? ") # Input em 2 linha como java
altura = float(input())

calcula_imc(peso = peso, altura = altura) # ou calcuma_imc(peso = 90, altura = 1.80) mesmo se inverter ele entende.
