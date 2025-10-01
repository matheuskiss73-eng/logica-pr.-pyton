import os
os.system("cls")

lista_notas = []



for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)


#print(f"Nota: {lista_notas}")
#print(f"Nota: {lista_notas[0]}")

for i in range(3):
    print(f"Nota: {lista_notas[i]}")

media = soma / 3
print(f"Media: {media}")


print("FIM")
