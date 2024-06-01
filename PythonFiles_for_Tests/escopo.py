x = 300 # variavel global

def myfunc():
    # para transformar essa var em global usamos
    # global x
    # com isso ele não vai dar erro por falta e uma variavel global
    x = 200 # Variavel local / se apagar essa no final ele vai usar a global
    print(x)
    
myfunc()
print(x)