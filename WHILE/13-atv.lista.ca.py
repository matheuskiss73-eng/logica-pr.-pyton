import os
os.system("cls")

print("""
código \t prato \t\t valor
      
 1 \t Picanha \t R$ 25,00
      
 2 \t Lazanha \t R$ 20,00
      
 3 \t Strogonoff \t R$ 18,00
      
 4 \t Bife Acebolado\t R$ 15,00
      
 5 \t Pão com ovo \t R$ 5,00
      
 6 \t Compra finalizada.
""")

soma = 0
valor = 0

while True:
    codigo = int(input("INFORME O CÓDIGO DO PRATO QUE DESEJA: "))

    if codigo == 6:
        break

    match codigo:
        case 1:
            valor = 25
        case 2:
            valor =  20
        case 3:
            valor = 18
        case 4:
            valor = 15
        case 5:
            valor = 5

    soma = soma + valor

if soma == 0:
    print("NENHUM PEDIDO FEITO!")
else:
    print("====== RECIBO ======")
    print(f"O valor total a pagar {soma}")
    print("OBRIGADO PELA ESCOLHA") 
