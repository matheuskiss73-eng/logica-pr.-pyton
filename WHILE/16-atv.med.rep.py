import os
os.system("cls")


quant_nts = 0
soma = 0
cont_nt = 0


while True:
    nota = float(input("Digite uma nota: "))
    quant_nts += 1
    soma += nota
    cont_nt += 1


    resposta = input("Deseja adicionar mais uma nota? \nUse S ou N para respoder: ").upper()


    if resposta == "N":
        break



media = soma / quant_nts

print(f"Sua média é: {media: .2f}")
print(f"Seu numero de notas é: {cont_nt}")