import login
import os

def gasolina():
    os.system('cls' if os.name == 'nt' else 'clear')
    login.carregar_interface("logo.txt")

    while(True):
        tipo = input("\n[ SISTEMA ]: Digite o tipo de combustivel (A-Álcool, G-Gasolina): ").upper()
        litros = float(input("\n[ SISTEMA ]: Digite a quantidade de litros vendidos: "))

        if tipo == 'A':
            valor = litros * 2.90
            if litros <= 20:
                total = valor - (valor * 0.03)
                print("\n[ SISTEMA ]: Desconto de 3% aplicado!")
            else:
                total = valor - (valor * 0.05)
                print("\n[ SISTEMA ]: Desconto de 5% aplicado!")
        elif tipo == 'G':
            valor = litros * 3.30
            if litros <= 20:
                total = valor - (valor * 0.04)
                print("\n[ SISTEMA ]: Desconto de 4% aplicado!")
            else:
                total = valor - (valor * 0.06)
                print("\n[ SISTEMA ]: Desconto de 6% aplicado!")
        else:
            print("\n[ SISTEMA ]: Tipo de combustivel invalido!")
            continue

        print(f"\n[ SISTEMA ]: O valor a ser pago e: R$ {total:.2f}")
        
        continuar = input("\n[ SISTEMA ]: Deseja continuar?[S/n]: ")
        
        if continuar != "n":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            break
