horas = float(input("Digite o total de horas trabalhadas no mês: "))
valor_hora = float(input("Digite o valor da hora: "))

# Limite mensal (40h por semana × 4 semanas)
horas_normais = 160

if horas <= horas_normais:
    salario = horas * valor_hora
else:
    horas_extra = horas - horas_normais
    valor_extra = valor_hora * 1.5
    
    salario = (horas_normais * valor_hora) + (horas_extra * valor_extra)


print("Salário total: R$", salario)