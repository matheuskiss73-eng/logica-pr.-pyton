import os
os.system("cls")

nome = input("digite seu nome: ")

n1 = float(input("digite o primeira nota : "))
n2 = float(input("digite o segunda nota : "))

media = (n1 + n2) / 2

if media >= 9:
    print (f"A. a sua média é {media}: APROVADO")

elif media >= 7.5 < 9:
    print (f"B. a sua média é {media}: APROVADO")

elif media >= 6 < 7.5: 
    print (f"C. a sua média é {media}: APROVADO")

elif media >= 4 < 6:
    print (f"D. a sua média é {media}; REPROVADO")

elif media <=4:
    print (f"E. a sua média é {media}: REPROVADO")

print(".") 