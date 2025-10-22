import os
os.system("cls")

def calc_imc(peso, altura):
    return peso / (altura ** 2)

def exibir(imc):
    print(f"Seu IMC é: {imc:.2f}")


peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

exibir(calc_imc(peso, altura))