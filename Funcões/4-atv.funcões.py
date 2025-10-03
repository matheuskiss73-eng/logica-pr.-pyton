import os
os.system("cls")


def tabuada(numero):
    for i in range (1,11):
        print(f"{numero} X {i} = {numero * i}")

numero = int(input("Digite um numero: "))

tabuada(numero)

