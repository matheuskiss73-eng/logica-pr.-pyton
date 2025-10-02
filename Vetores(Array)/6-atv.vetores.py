import os
os.system("cls")

lista_numeros = []
negativos = 0
positivos = []
soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)




for i in lista_numeros:
    if i < 0:
        negativos += 1
    else:
        positivos.append(negativos)


print(f"Quantidade de numeros negativos: {negativos}")
print(f"Soma dos positivos {sum(positivos)}")
print("FIM")