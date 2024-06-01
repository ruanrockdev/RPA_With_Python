while True:
    print("Qual é o nome certo ?")
    sName = input()
    if sName != "José":
        continue
    print("Olá José, digite sua senha:")
    sSenha = input()
    if sSenha == "123":
        break
            
print("Fim do Programa!")
