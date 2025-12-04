import os
import time 
from dataclasses import dataclass

os.system("cls || clear")

lista_clientes = [] 
lista_produtos = [] 

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Produto:
    nomep: str
    quantidade: str
    lote: str
    validade: str
    
    def mostrar_dados(self):
        return (f"Produto: {self.nomep}\nQuantidade: {self.quantidade}\nLote: {self.lote}\nValidade: {self.validade}\n")

# Funções de Produto
def lista_produtos_esta_vazia(lista_produtos):
    if not lista_produtos:
        print("\nNão há Produtos cadastrados.")
        return True
    return False

def adicionar_produto(lista_produtos):
    print("\n--- Adicionar novo produto ---")
    nome = input("Digite o nome produto: ")
    quantidade = input("Digite a quantidade de produtos: ")
    lote = input("Digite o lote do produto: ")
    validade = input("Digite a validade: ")
    
    novo_produto = Produto(nomep=nome, quantidade=quantidade, lote=lote, validade=validade)
    lista_produtos.append(novo_produto)
    print(f"\nProduto {nome} adicionado com sucesso!")

def encontrar_produto_por_nome(lista_produtos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for produto in lista_produtos:
        if produto.nomep.lower() == nome_buscar_lower:
            return produto
    return None 

def mostrar_todos_produto(lista_produtos):
    if lista_produtos_esta_vazia(lista_produtos):
        return
    print("\n--- Lista de produtos ---")
    for produto in lista_produtos:
        print(produto.mostrar_dados())

def atulizar_produto(lista_produtos):
    if lista_produtos_esta_vazia(lista_produtos):
        return

    mostrar_todos_produto(lista_produtos) 
    print("====== Atualizar dados do produto ======") 
    produto_buscar = input("\nDigite o nome do produto que deseja atualizar: ")
    produto_para_atualizar = encontrar_produto_por_nome(lista_produtos, produto_buscar)

    if produto_para_atualizar:
        print("\nDigite os novos dados ou deixe em branco para manter os atuais.")

        print(f"\nProduto atual: {produto_para_atualizar.nomep}") 
        novo_nome = input("Novo produto: ")
        if novo_nome:
            produto_para_atualizar.nomep = novo_nome 
            
        print(f"Quantidade atual: {produto_para_atualizar.quantidade}")
        novo_quantidade = input("Nova Quantidade: ")
        if novo_quantidade:
            produto_para_atualizar.quantidade = novo_quantidade

        print(f"Lote atual: {produto_para_atualizar.lote}")
        novo_lote = input("Novo Lote: ")
        if novo_lote:
            produto_para_atualizar.lote = novo_lote
        
        print(f"Validade atual: {produto_para_atualizar.validade}")
        novo_validade = input("Nova Validade: ")
        if novo_validade:
            produto_para_atualizar.validade = novo_validade
        
        print(f"\nDados do produto **{produto_buscar}** atualizados com sucesso!")
        
    else:
        print(f"\nProduto: {produto_buscar} não encontrado.")


def excluir_produto(lista_produtos):
    if lista_produtos_esta_vazia(lista_produtos):
        return
    mostrar_todos_produto(lista_produtos)

    nome_buscar = input("\nDigite o nome do produto que deseja excluir: ") 

    produtos_para_remover = encontrar_produto_por_nome(lista_produtos, nome_buscar)
    
    if produtos_para_remover:
        lista_produtos.remove(produtos_para_remover)
        print(f"\nProduto **{produtos_para_remover.nomep}** excluído com sucesso!") 
    else:
        print(f"\nProduto **{nome_buscar}** não encontrado.")


#=========================================================================================================
#=========================================================================================================
#=========================================================================================================

@dataclass
class Clientes:
    nome: str 
    email: str
    tefone: str
    endereco: Endereco

    def mostrar_dados(self):
        return (f"Nome: {self.nome}\nEmail: {self.email}\nTelefone: {self.tefone}\n"
                f"Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade} - {self.endereco.estado}\n")

def lista_clientes_esta_vazia(lista_clientes): 
    if not lista_clientes:
        print("\nNão há Clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista_clientes): 
    print("\n--- Adicionar novo Cliente ---")
    nome = input("Digite o nome: ")
    email = input("Digite o email: ") 
    tefone = input("Digite o telefone: ")
    
    while True:
        try:
            numero = int(input("Digite o número do endereço: "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número para o número do endereço.")
    
    logradouro = input("Digite o logradouro: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    
    endereco = Endereco(logradouro=logradouro, numero=numero, cidade=cidade, estado=estado)
    # Cria o objeto Clientes usando os campos corretos
    novo_cliente = Clientes(nome=nome, email=email, tefone=tefone, endereco=endereco)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente **{nome}** adicionado com sucesso!")

def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None 

def mostrar_todos_cliente(lista_clientes): 
    if lista_clientes_esta_vazia(lista_clientes):
        return
    print("\n--- Lista de Clientes ---")
    for cliente in lista_clientes:
        print(cliente.mostrar_dados())

def atulizar_cliente(lista_clientes):
    if lista_clientes_esta_vazia(lista_clientes):
        return

    mostrar_todos_cliente(lista_clientes)
    print("====== Atualizar dados do Cliente ======")
    cliente_buscar = input("\nDigite o nome do cliente que deseja atualizar: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, cliente_buscar)

    if cliente_para_atualizar:
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")
        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
            
        print(f"Email atual: {cliente_para_atualizar.email}") 
        novo_email = input("Novo Email: ")
        if novo_email:
            cliente_para_atualizar.email = novo_email

        print(f"Telefone atual: {cliente_para_atualizar.tefone}")
        novo_tefone = input("Novo Telefone: ")
        if novo_tefone:
            cliente_para_atualizar.tefone = novo_tefone
            
        print("\n--- Atualizar Endereço (Deixe em branco para manter) ---")
        
        print(f"Logradouro atual: {cliente_para_atualizar.endereco.logradouro}")
        novo_logradouro = input("Novo logradouro: ")
        if novo_logradouro:
            cliente_para_atualizar.endereco.logradouro = novo_logradouro
            
        print(f"Número atual: {cliente_para_atualizar.endereco.numero}")
        novo_numero_str = input("Novo número: ")
        if novo_numero_str:
            try:
                cliente_para_atualizar.endereco.numero = int(novo_numero_str)
            except ValueError:
                print("\n**ATENÇÃO:** O número digitado é inválido. Mantendo o valor anterior.")
                
        print(f"Cidade atual: {cliente_para_atualizar.endereco.cidade}")
        nova_cidade = input("Nova cidade: ")
        if nova_cidade:
            cliente_para_atualizar.endereco.cidade = nova_cidade

        print(f"Estado atual: {cliente_para_atualizar.endereco.estado}")
        novo_estado = input("Novo estado: ")
        if novo_estado:
            cliente_para_atualizar.endereco.estado = novo_estado


        print(f"\nDados do cliente **{cliente_buscar}** atualizados com sucesso!")
        
    else:
        print(f"\nCliente com nome: **{cliente_buscar}** não encontrado.")


def excluir_cliente(lista_clientes): 
    if lista_clientes_esta_vazia(lista_clientes):
        return
    mostrar_todos_cliente(lista_clientes)

    nome_buscar = input("\nDigite o nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_buscar)
    
    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente **{cliente_para_remover.nome}** excluído com sucesso!")
    else:
        print(f"\nCliente com o nome **{nome_buscar}** não encontrado.")


while True:
    print("""
===============================
====EMPRESA MAMÃO com AÇÚCAR===
===============================
=== Gerenciador de Clientes ===
1 - Adicionar Cliente
2 - Mostrar todos os Clientes
3 - Atualizar Cliente
4 - Excluir Cliente

=== Gerenciador de Produtos   ===
5 - Adicionar Produtos
6 - Mostrar todos os Produtos
7 - Atualizar Produto
8 - Excluir Produto

=== FINALIZAR SITE ===

0 - Sair
          """)
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada inválida. Digite um número.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_cliente(lista_clientes) 
            time.sleep(1)
            os.system("cls || clear")
        case 2:
            mostrar_todos_cliente(lista_clientes) 
            time.sleep(4)
        case 3:
            atulizar_cliente(lista_clientes) 
            time.sleep(4)
        case 4:
            excluir_cliente(lista_clientes) 
            time.sleep(4)
        case 5:
            adicionar_produto(lista_produtos)
            time.sleep(1)
            os.system("cls || clear")
        case 6:
            mostrar_todos_produto(lista_produtos)
            time.sleep(4)
        case 7:
            atulizar_produto(lista_produtos)
            time.sleep(4)
        case 8:
            excluir_produto(lista_produtos)
            time.sleep(4)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(2)
    
    if opcao != 0 and opcao not in (1, 5):
        os.system("cls || clear")
        
        
        #depois revise