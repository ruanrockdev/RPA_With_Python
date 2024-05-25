def calc_sal(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <= 40:
        salario = horas * taxa
    else:
        horasMais = horas - 40
        salario = 40 * taxa + (horasMais * (1.5*taxa))
    return salario


str_horas = input("Digite a quantidade de horas trabalhadas: ")
str_taxa = input("Digite a taxa: (valor da hora)")

salario_calculado = calc_sal(str_horas, str_taxa)
print("o valor do salário é R$ ", salario_calculado)
