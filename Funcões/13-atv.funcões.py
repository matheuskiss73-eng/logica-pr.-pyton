import os 
import time
os.system("cls")

lista_notas = []

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / 2
    return resultado

def resultado_final(media):
    if media <=7:
        print("aprovado")
    else:
        print("falied")

for i in range(2):
    while True:
        nota = float(input("Digite uma nota: "))
        if  nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:
            print("Nota invalida! tente novamente...")
            time.sleep(2)



media = calcular_media(lista_notas)

print(f"Média: {media:.2f}")
resultado_final(media)