import os
os.system("cls")

dia = int(input("digite um numero para um dia da semana: "))

match dia:
    case 1:
        print("domingo FIM DE SEMANA")
    case 2:
        print("segunda-feira DIA ÚTIL")
    case 3:
        print("terça-feira DIA ÚTIL")
    case 4:
        print("quarta-feira DIA ÚTIL")
    case 5:
        print("quinta-feira DIA ÚTIL")
    case 6: 
        print("sexta-feira DIA ÚTIL")
    case 7:
        print("sábado FIM DE SEMANA")
    case _:
        print("opção invalida.")

print("FIM")