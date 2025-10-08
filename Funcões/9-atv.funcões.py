import os
os.system("cls")

def centimetros(altura):
    return altura * 100

altura = float(input(f"Digite sua altura (Ex: 1.83): "))

altura = centimetros(altura)

print(f"Você tem {altura} cm")