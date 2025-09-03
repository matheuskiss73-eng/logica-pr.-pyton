import os
os.system("cls")

numero1 = float(input("digite o primeiro numero: "))
numero2 = float(input("digite o segundo numero: "))

soma = numero1 + numero2
produto = numero1 * numero2



maior = max(numero1, numero2)
menor = min(numero1, numero2)


print(f"soma:", soma)
print(f"produto:", produto)
print(f"maior_numero:", maior)
print(f"menor_numero:", menor)

