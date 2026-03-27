nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): "))
sexo = input("Digite seu sexo (M/F): ").upper()

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Sexo inválido!")
    peso_ideal = None

if peso_ideal is not None:
    print(f"Nome: {nome}")
    print(f"Peso ideal: {peso_ideal:.2f} kg")