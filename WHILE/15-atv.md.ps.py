import os
os.system("cls")



quan_nts = 0
soma = 0


while True:
    nota = float(input("Digite uma nota : "))
    quan_nts += 1
    if nota < 0:

        quan_nts -= 1
        break
    else:
        soma += nota
        media = soma / quan_nts
        

print(f"Sua média é: {media: .2f}")     


