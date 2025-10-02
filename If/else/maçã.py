import os
os.system("cls")
quant = float(input("digite quantas maçãs deseja: "))

md = quant * 1.3

if quant <= 12:
    print(f"você comprou {quant} com o preço R${md: .2f} reais")

elif quant >= 12: 
    print(f"você comprou {quant} com preço R${quant} reais")
    
print("FIM")    