import os
os.system("CLS")

usuario1 = "matheus"
senha1 = "123456"
tentativas = 3

for tentativa in range(tentativas):
    print(f"Tentativa {tentativa + 1} de {tentativas}")


    usuario = input("digite o nome do usuario: ")
    senha = input("digite sua senha: ")

    if usuario == usuario1 and senha == senha1:
        print("Seja Bem vindo")
        break
    
    else:
        print("login ou senha invalidos")    

else:
    print("Você excedeu o número de tentativas. Acesso negado.")