import os
os.system("cls")


quan_nts = 0
soma = 0


while True:
    nota = float(input("Digite uma nota : "))
    quan_nts +=1
    soma += nota

    resposta = input("Deseja adicionar mais uma nota? \nUse S ou N para responder: ").upper()
    
    if resposta == "N":
        break

media = soma /quan_nts


print(f"Sua média é: {media}")