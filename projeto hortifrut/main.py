import os
import login
import time
import produtos
import gasolina
import frutas

# 1. Limpa e mostra o layout
os.system("cls" if os.name == "nt" else "clear")

# 2. Animaçãozinha inicial (fora do clear para o usuário ver)
print(" [ SISTEMA ]: Carregando banco de dados...")
time.sleep(0.5) 
print(" [ SISTEMA ]: Verificando integridade dos arquivos...")
time.sleep(0.5)

os.system("cls" if os.name == "nt" else "clear")

login.carregar_interface("logo.txt")
login.logica()

os.system("cls" if os.name == "nt" else "clear")
print(" [ SISTEMA ]: Verificando integridade dos arquivos...")
time.sleep(2)
os.system("cls" if os.name == "nt" else "clear")

login.carregar_interface("logo.txt")

while(True):
    login.carregar_interface("tiao.txt")
    
    try:
        servico = int(input("  > NUMERO DO DEPARTAMENTO: "))
        
        if servico == 1:
            produtos.produtos()
            
        elif servico == 2:
            gasolina.gasolina()
            
        elif servico == 3:
            frutas.frutas()
            
        elif servico < 1 or servico > 3:
          print("[ SISTEMA ]: O numero que voce digitou, desligara o sistema. (Opcoes: 1-Produtos, 2-Gasolina, 3-Frutas)")
          break
            
        
    except ValueError:
            # Se o usuário digitou letras ou deixou vazio
            print("\n [ SISTEMA ] ERRO DE DIGITAÇÃO: Por favor, use apenas NÚMEROS.")
            print(" [ SISTEMA ] O sistema do Tião não aceita letras no peso da carga.\n")
    
    
    
    
    
os.system("cls" if os.name == "nt" else "clear")
print("\n [ SISTEMA ]: Finalizando processos do Tião Inc", end="", flush=True)
for _ in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)

# Exibe a mensagem final estilizada
print(f"""

==================================================
  LOGOUT EFETUADO COM SUCESSO.
  VOLTE SEMPRE AO POMAR TECNOLÓGICO!
==================================================
""")
time.sleep(2)
os.system("cls" if os.name == "nt" else "clear")
exit() # Encerra o programa Python definitivamente