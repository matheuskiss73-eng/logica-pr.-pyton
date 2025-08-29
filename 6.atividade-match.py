import os
os.system("cls")

operação = input("digite a operção: ")
nu1 = int(input("digite o primeiro numero: "))
nu2 = int(input("digite o segundo numero: "))

match operação:
    case "+":
        print("soma esc")
        print("resultado:",  nu1 + nu2)
    case "-":
        print("subtração esc")
        print("resultado:",  nu1 - nu2)
    case "*":
        print("multiplicação esc")
        print("resultado:",  nu1 * nu2)
    case "/":  
        print("divisão esc")
        print("resultado:",  nu1 / nu2)
    case "_":
        print("opçao inválida")

print("FIM")