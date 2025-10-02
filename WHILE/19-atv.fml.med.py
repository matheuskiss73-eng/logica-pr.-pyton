import os
os.system("cls")



soma = 0
quantidade_salarios = 0
menor_salario = 0
maior_salario = 0
salario = 0
filhos = 0


while True:
    print("""
    CODIGO\t MENU
    1   | Adicionar familia
    2   | Sair e exibir resultados
""")
    

    codigo = int(input("INFORME O CÓDIGO: "))
    match codigo:
        case 1:
           filhos = int(input("Digite numero filhos: "))
           salario = float(input("Digite o valor salário: "))
             
           quantidade_salarios += 1
           soma_salario += salario

            
           if salario < menor_salario:
            menor_salario = salario

           if salario > maior_salario:
            maior_salario = salario



        case 2:
            media_salarial = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
            if me == 9999:
                me = 0
               
            print("\n= Exibindo resultados =")
            print(f"Média de salários do grupo: {media_salarial}")
            print(f"Menor idade do grupo: {menor_idade}")
            print(f"Maior idade do grupo: {maior_idade}")
            print(f"Quantidade de mulheres com salário acima de 5 mil: {mulheres5k}")
            input("Pressione enter para continuar...")
        case 3:
            print("Saindo do programa.")
            input("Pressione enter para sair...")
            break
        case _:
            print("Opção inválida, tente novamente.")
            input("Pressione enter para continuar...")