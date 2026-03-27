import os
import time

def carregar_interface(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as arquivo:
            layout = arquivo.read()
            print(layout)
            return layout
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        return False


# --- FLUXO PRINCIPAL DO PROGRAMA (AGORA FORA DA FUNÇÃO) ---
def logica():
    CODIGO_CORRETO = "1234"
    SENHA_CORRETA = "9999"
    
    print("\nSISTEMA DE GESTÃO DE SAFRA - ACESSO RESTRITO:")

    while True:
        codigo_usuario = input("  > CÓDIGO DO COLABORADOR: ")
        
        if codigo_usuario != CODIGO_CORRETO:
            print("\n [!] Usuário inválido! Tente novamente.")
            time.sleep(2) # Pausa para o usuário ler o erro antes de limpar a tela
        else:
            senha_digitada = input("  > SENHA DO COLABORADOR: ")

            print(" [ SISTEMA ]: Conectando ao pomar", end="", flush=True)
            for _ in range(3):
                time.sleep(0.5)
                print(".", end="", flush=True)
            print(" [ OK ]") # Pula a linha no final

            if senha_digitada == SENHA_CORRETA:

                print("\n [ SISTEMA ]: Autenticação bem-sucedida. Bem-vindo(a)!")
                print("\n---------------------------------------------------------")
                print("   © 2026 TIÃO DA LARANJA ENTERPRISES - GLOBAL DIVISION")
                print("=========================================================")
                time.sleep(2)
                break # Sai do loop while
            else:
                print("\n [!] Senha incorreta!")
