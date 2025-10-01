import os
os.system("cls")

lista_notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)


for i in range(4):
    print(f"Nota: {lista_notas[i]}")


media = soma / 4
print(f"Media: {media:.2f}")


if media >=7 :
        print ("VOCÊ FOI APROVADO  PARABÉNS!!!")

elif media >= 5.1 < 6.9:
    print ("VOCÊ ESTÁ DE RECUPERAÇÃO")

elif media >= 5:
    print ("VOCÊ FOI REPROVADO")




print("FIM")