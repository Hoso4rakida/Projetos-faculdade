import login
import os

def frutas():
    os.system('cls' if os.name == 'nt' else 'clear')
    login.carregar_interface("logo.txt")

    while(True):
        kg_morango = float(input("\n[ SISTEMA ]: Digite a quantidade de morangos (Kg): "))
        kg_maca = float(input("\n[ SISTEMA ]: Digite a quantidade de macas (Kg): "))

        if kg_morango <= 5:
            preco_morango = 2.50
        else:
            preco_morango = 2.20

        if kg_maca <= 5:
            preco_maca = 1.80
        else:
            preco_maca = 1.50

        valor_morango = kg_morango * preco_morango
        valor_maca = kg_maca * preco_maca

        total_kg = kg_morango + kg_maca
        valor_bruto = valor_morango + valor_maca

        if total_kg > 8 or valor_bruto > 25.00:
            valor_final = valor_bruto * 0.90
            print("\n[ SISTEMA ]: Desconto de 10% aplicado!")
        else:
            valor_final = valor_bruto

        print(f"\n[ SISTEMA ]: Total de quilos: {total_kg:.2f} Kg")
        print(f"[ SISTEMA ]: Valor a ser pago: R$ {valor_final:.2f}")

        continuar = input("\n[ SISTEMA ]: Deseja continuar?[S/n]: ")
        
        if continuar != "n":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
