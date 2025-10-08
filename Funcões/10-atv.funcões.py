import os
os.system("cls")

def valor(preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20
    

preco = float(input("Diga o preço do seu produto: "))
total = valor(preco)


print(f"o valor final do seu produto com inflção aplicada é: {total}")