numeroCT = int(input("Informe o número da sua conta: "))
saldo = float(input("Informe o seu saldo: "))
credito = float(input("Informe o valor do seu crédito: "))
debito = float(input("Informe o valor do seu débito: "))

saldoATL = saldo - debito + credito

print(f"Saldo atual: R$ {saldoATL:.2f}")

if saldoATL >= 0:
	print("Seu saldo está positivo.")
else:
	print("Seu saldo está negativo.")