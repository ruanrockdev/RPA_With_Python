# Encontrando padrão sem Regex (DD) XXXXX-XXXX
# Alterei

def is_phone_number(text):
    if len(text) != 15:
        return False
    if text[0] != "(":
        return False
    for i in range(1, 3):
        if not text[i].isdecimal():
            return False
    if text[4] != " ":
        return False
    for i in range(5, 10):
        if not text[i].isdecimal():
            return False
    if text[10] != "-":
        return False
    for i in range(11, 15):
        if not text[i].isdecimal():
            return False
    return True


print(is_phone_number("valida telefone"))
print(is_phone_number("(21) 91234-1234"))
