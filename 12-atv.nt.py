import os
os.system("cls")

nome = input("digite seu nome: ")

n1 = float(input("digite o primeira nota : "))
n2 = float(input("digite o segunda nota : "))
n3 = float(input("digite o terceira nota : "))

media = (n1 + n2 + n3) / 3

if media >=7 :
        print (f"a sua média é {media:.2f}: VOCÊ FOI APROVADO  PARABÉNS!!! {nome}")

elif media >= 5.1 < 6.9:
    print (f"a sua média é {media:.2f}; VOCÊ ESTÁ DE RECUPERAÇÃO")

elif media >= 5:
    print (f"a sua média é {media:.2f}; VOÊ FOI REPROVADO")



print(".") 