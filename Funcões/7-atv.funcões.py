import os
import time

os.system("cls")

# função sem pârametros sem retorno
def limpa_tela():
    time.sleep(3) #espera 3 segundo.
    os.system("cls")


# função com parametros e com retorno
def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media
# função com parametros e com retorno
def mostrar_resu(media):
    print(F"Resultado: {media}")
    if media>= 7:
        print(f"Aprovado")
    else:
        print(f"Reprovado")


#codigo principal.
# função sem parametros e sem retorno
limpa_tela() # chamado de função.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

media = calcular_media(n1, n2)

# função com parametros e com retorno
mostrar_resu(media) #chamando a função