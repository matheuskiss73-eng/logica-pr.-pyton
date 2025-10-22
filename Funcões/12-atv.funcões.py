import os
os.system("cls")


lista_notas = []

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / 3
    return resultado

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)



media = calcular_media(lista_notas)

print(f"Média: {media:.2f}")