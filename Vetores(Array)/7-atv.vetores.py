import os
os.system("cls")

contador = 0
numeros = []


while True:
    numero = float(input(f"Digite o {contador+1}º numero: "))
    contador += 1

    if numero < 0:
        numero = 0
        numeros.append(numero)
    else:
        numeros.append(numero)
    if contador >= 5:
        break
print(f"LISTA: {numeros}")