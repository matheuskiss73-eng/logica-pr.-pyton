import os
os.system("cls")



while True:
    nota = float(input("Digite uma nota: "))

    if nota <=10 and nota >= 0:
        break
    print(f"Sua nota é: {nota}")