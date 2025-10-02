import os
os.system("cls")



lista_numeros = []
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)



for i in lista_numeros:    
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1



print(f"numero: {lista_numeros}")
print(f"\nQuantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print("FIM")