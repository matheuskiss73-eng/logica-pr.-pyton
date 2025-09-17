import os
os.system("CLS")

usuario1 = "matheus"
senha1 = "123456"

usuario = input("digite o nome do usuario: ")
senha = input("digite sua senha: ")

if usuario == usuario1 and senha == senha1:
    print("Seja Bem vindo")
else:
    print("login ou senha invalidos")    