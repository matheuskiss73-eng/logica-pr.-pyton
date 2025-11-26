import os 
os.system("cls")

lista_clientes = []
# CREATE
print("CREATE - Adicionar / Inserir")
nome = "Matheus"
lista_clientes.append(nome)
print(f"0 nome: {nome} foi inserido com sucesso!")

# READ
print("\nRead -Ler / Mostrar")
print(lista_clientes)

# UPDATE
print("\nUpdate -Atualizar / Alterar")
nome_para_atualizar = "Matheus"
if nome_para_atualizar in lista_clientes:
    novo_nome = "Matheus Silva"
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes [indice]= novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)
# DELETE
print("\nDelete - Deletar / Remover")
nome_para_excluir = "Matheus"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"O nome {nome_para_excluir} foi removido com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)

while True:
    os.system("cls")
    print(""""
Código   |   Descrição
   1     | CREATE
   2     | READ    
   3     | UPDATE
   4     | DELETE
   0     | Sair
""")
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            print("CREATE - Adicionar / Inserir")
            nome = input("Informe o nome para adicionar: ")
            lista_clientes.append(nome)
            print(f"O nome: {nome} foi inserido com sucesso!")
            input("Pressione enter para continuar...")
        case 2:
            print("\nRead -Ler / Mostrar")
            print(lista_clientes)
            input("Pressione enter para continuar...")
        case 3:
            print("\nUpdate -Atualizar / Alterar")
            nome_para_atualizar = input("Informe o nome para atualizar: ")
            if nome_para_atualizar in lista_clientes:
                novo_nome = input("Informe o novo nome: ")
                indice = lista_clientes.index(nome_para_atualizar)
                lista_clientes [indice]= novo_nome
                print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}")
            else:
                print(f"O nome {nome_para_atualizar} não foi encontrado.")
            input("Pressione enter para continuar...")
        case 4:
            print("\nDelete - Deletar / Remover")
            nome_para_excluir = input("Informe o nome para excluir: ")
            if nome_para_excluir in lista_clientes:
                lista_clientes.remove(nome_para_excluir)
                print(f"O nome {nome_para_excluir} foi removido com sucesso!")
            else:
                print(f"O nome {nome_para_excluir} não foi encontrado.")
            input("Pressione enter para continuar...")
        case 0:
            print("Saindo do programa.")
            input("Pressione enter para sair...")
            break
        case _:
            print("Opção inválida, tente novamente.")
            input("Pressione enter para continuar...")