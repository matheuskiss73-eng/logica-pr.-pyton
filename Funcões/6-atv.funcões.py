import os
import time

os.system("cls")

# função sem pârametros sem retorno
def limpa_tela():
    time.sleep(3) #espera 3 segundo.
    os.system("cls")


# função com parametros e com retorno
def somar(n1, n2):
    calcular = n1 + n2
    return calcular
# função com parametros e com retorno
def mostrar_resu(soma):
    print(F"Resultado: {soma}")


#codigo principal.
# função sem parametros e sem retorno
limpa_tela() # chamado de função.
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

# função com parametros e com retorno
soma = somar(n1, n2)
mostrar_resu(soma) #chamando a função