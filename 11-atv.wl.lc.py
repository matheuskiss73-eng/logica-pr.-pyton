import os
os.system("cls")


QUANTIDADE_NOTAS =  2
soma = 0


for i in range(QUANTIDADE_NOTAS):
    while True:
        n1 = int(input(f"Digite a {i+1}ª: "))

        if n1 <=10 and n1 >= 0:
            break
    
    soma =  soma +  n1

media = soma / QUANTIDADE_NOTAS


print(f"Sua média é: {media}")