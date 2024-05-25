def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Invalid Argument.")
    except TypeError:
        print("Error: Invalid Type.")
    finally:
        print("Função Finalizada")
    
print(division(20, 2))
print(division(12, "a"))
print(division(5, 0))
print(division(1, 3))

