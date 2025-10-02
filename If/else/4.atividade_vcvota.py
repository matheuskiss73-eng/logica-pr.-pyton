import os
os.system("cls")

idade = int(input('digite sua idade: '))

if  idade < 18 or idade > 65:
    print("você não é obrigado a votar")
else:
    print("votação obrigatoria")   