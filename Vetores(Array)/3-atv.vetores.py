import os
os.system("cls")

lista_numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)


for i in range(5):
    print(f"Numeros: {lista_numeros[i]}")


maior = max(lista_numeros)
menor = min(lista_numeros)

print(f"Esse é o maior numero: {maior}")
print(f"Esse é o menor numero: {menor}")
print("FIM")