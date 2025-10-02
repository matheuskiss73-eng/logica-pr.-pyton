import os
os.system("cls")


lista_codigos = []
pratos = []
valores = []

print("""
código \t prato \t\t valor
      
 1 \t Picanha \t R$ 25,
      
 2 \t Lazanha \t R$ 20,00
      
 3 \t Strogonoff \t R$ 18,00
      
 4 \t Bife Acebolado\t R$ 15,00
      
 5 \t Pão com ovo \t R$ 5,00
""")

while True:
    codigo = int(input("INFORME O CÓDIGO DO PRATO QUE DESEJA: "))
    lista_codigos.append(codigo)
    
    if codigo == 0:
        break

    match codigo:
        case 1:
            prato = "Picanha"
            valor = 25
        case 2:
            prato = "Lazanha"
            valor =  20
        case 3:
            prato = "Strogonoff"
            valor = 18
        case 4:
            prato = "Bife Acebolado"
            valor = 15
        case 5:
            prato = "Pão com ovo"
            valor = 5



    resposta = input("Deseja adicionar mais um pedido? \nUse S ou N para respoder: ").upper()

    pratos.append(prato)
    valores.append(valor)
    os.system("cls")    
    if resposta == "N":
        break


print("====== RECIBO ======")
for prato in pratos:
    print(f"Prato: {prato}")
for valor in valores:
    print(f"valores: {valor}")
print(f"valor a pagar: {sum(valores)}")