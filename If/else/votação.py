import os
os.system("cls")



idade = int(input('digite sua idade: '))

if idade >= 18:
    print("votação obrigatoria")

elif idade>= 65:
     print("você não é obrigado a votar")

elif idade >= 16:
    print("seu voto é opcional") 

elif idade >= 17:
    print("seu voto é opcional")       

elif idade < 16:
      print("Você não pode votar (menor de idade)")

print("FIM")