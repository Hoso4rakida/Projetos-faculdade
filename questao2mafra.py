anoat = int(input("Informe o ano Atual: "))
anons = int(input("Informe o seu ano de nascimento: "))

idade = anoat - anons

if idade >= 16:
	print("Você está apto para votar.")
else:
	print("Você não está apto para votar.")