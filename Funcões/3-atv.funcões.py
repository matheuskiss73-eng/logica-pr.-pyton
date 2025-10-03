import os 
os.system("cls")

def posi_nega(numero):
    if numero < 0:
        print("Negativo")

    else:
        print("Positivo")
    
numero = int(input("Digite um numero: "))
posi_nega(numero)