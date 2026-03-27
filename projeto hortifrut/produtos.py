import login
import os

def produtos():
    os.system('cls' if os.name == "nt" else "clear")
    login.carregar_interface("logo.txt")
    
    while(True):
        nome = input("\n[ SISTEMA ]: Digite o nome do produto: ")
        quantidade = int(input("\n[ SISTEMA ]: Digite quantos pretende levar?: "))
        preco = float(input("\n[ SISTEMA ]: Qual valor unitario que mostra no produto?: "))
        valor = preco * quantidade
        total = 0
        
        if quantidade <= 5:
            total = valor - (valor * 0.02)
            print("\n[ SISTEMA ]: Você recebera um desconto de 2%! ")
        elif quantidade > 5 and quantidade <= 10:
            total = valor - (valor * 0.03)
            print("\n[ SISTEMA ]: Você recebera um desconto de 3%! ")
        elif quantidade > 10:
            total = valor - (valor * 0.05)
            print("\n[ SISTEMA ]: Você recebera um desconto de 5%! ")
            
            
        
        print(f"\n[ SISTEMA ]: você pagara: R$ {total} em {nome}")
        continuar = input("\n[ SISTEMA ]: Deseja continuar?[S/n]: ")
        
        if continuar != "n":
            os.system('cls' if os.name == "nt" else "clear")
        else:
            break
            