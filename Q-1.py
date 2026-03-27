quantidade = int(input('Quantas maçãs você comprou? '))

if quantidade < 12:
    preço = 1.30
else:
    preço = 1.00

total = quantidade * preço
print (f'Sua compra ficou: {total}')