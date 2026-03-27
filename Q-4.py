salario_fixo = float(input('Digite o salario fixo: '))
vendas = float(input('Digite o Valor das vendas: '))

if vendas <= 1500:
    comissão = vendas * 0.03
else:
    comissão = (1500 * 0.03) + ((vendas - 1500)* 0.05)

salario_total = salario_fixo + comissão

print(f'Salario Total: {salario_total:.2f}')