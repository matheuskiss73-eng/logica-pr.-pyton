import os
os.system("cls")

def somar(n1, n2):
    calcular = n1 + n2
    return calcular

def mostrar_resu_sm(soma):
    print(F"Resultado da soma: {soma}")

def subtracao(n1, n2):
    calcular = n1 - n2
    return calcular

def mostrar_resu_sb(subtracao):
    print(F"Resultado da subtrção: {subtracao}")

def divisao(n1, n2):
    calcular = n1 / n2
    return calcular

def mostrar_resu_dv(divisao):
    print(F"Resultado da divisão: {divisao}")

def multiplicacao(n1, n2):
    calcular = n1 * n2
    return calcular

def mostrar_resu_mt(multiplicacao):
    print(F"Resultado da multiplicação: {multiplicacao}")


n1 = float(input("Digite um numero: "))
n2 = float(input("Digite um numero: "))


soma = somar(n1, n2)
subtracao = subtracao(n1, n2)
divisao = divisao(n1, n2)
multiplicacao = multiplicacao(n1, n2)

mostrar_resu_sm(soma)
mostrar_resu_sb(subtracao)
mostrar_resu_dv(divisao)
mostrar_resu_mt(multiplicacao)