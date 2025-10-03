import os
os.system("cls")

def par_impa(numero):
    if numero % 2 == 0:
        print("Esse numero é par")
    else:
        print("Esse numero é impa")
    


numero = float(input(f"Digite um numero: "))
par_impa(numero)