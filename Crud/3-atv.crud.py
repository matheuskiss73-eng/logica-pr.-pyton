import os
import time 
from dataclasses import dataclass

os.system("cls || clear")

lista_alunos = []

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str
    estado: str

@dataclass
class Aluno:
    nome: str 
    data: str
    ra: str
    curso: str
    endereco: Endereco
    
    def mostrar_dados(self):
        return (f"Nome: {self.nome}\nData de nascimento: {self.data}\nR.A.: {self.ra}\nCurso: {self.curso}\n"
                f"Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade} - {self.endereco.estado}\n")

def lista_esta_vazia(lista_alunos):
    if not lista_alunos:
        print("\nNão há Alunos cadastrados.")
        return True
    return False

def adicionar_aluno(lista_alunos):
    print("\n--- Adicionar novo Aluno ---")
    nome = input("Digite o nome: ")
    data = input("Digite a Data de nascimento: ")
    ra = input("Digite o R.A.: ")
    curso = input("Digite o Curso: ")
    
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
    novo_aluno = Aluno(nome=nome, data=data, ra=ra, curso=curso, endereco=endereco)
    lista_alunos.append(novo_aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")

def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_buscar_lower:
            return aluno
    return None 

def mostrar_todos_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    print("\n--- Lista de alunos ---")
    for aluno in lista_alunos:
        print(aluno.mostrar_dados())

def atulizar_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return

    mostrar_todos_aluno(lista_alunos)
    print("====== Atualizar dados do aluno ======")
    aluno_buscar = input("\nDigite o nome do aluno que deseja atualizar: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, aluno_buscar)

    if aluno_para_atualizar:
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"\nNome atual: {aluno_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")
        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
            
        print(f"Data de nascimento atual: {aluno_para_atualizar.data}")
        novo_data = input("Nova data: ")
        if novo_data:
            aluno_para_atualizar.data = novo_data

        print(f"R.A. atual: {aluno_para_atualizar.ra}")
        novo_ra = input("Novo R.A.: ")
        if novo_ra:
            aluno_para_atualizar.ra = novo_ra
        
        print(f"Curso atual: {aluno_para_atualizar.curso}")
        novo_curso = input("Novo curso: ")
        if novo_curso:
            aluno_para_atualizar.curso = novo_curso
            
        print("\n--- Atualizar Endereço (Deixe em branco para manter) ---")
        
        print(f"Logradouro atual: {aluno_para_atualizar.endereco.logradouro}")
        novo_logradouro = input("Novo logradouro: ")
        if novo_logradouro:
            aluno_para_atualizar.endereco.logradouro = novo_logradouro
            
        print(f"Número atual: {aluno_para_atualizar.endereco.numero}")
        novo_numero_str = input("Novo número: ")
        if novo_numero_str:
            try:
                aluno_para_atualizar.endereco.numero = int(novo_numero_str)
            except ValueError:
                print("\n**ATENÇÃO:** O número digitado é inválido. Mantendo o valor anterior.")
                
        print(f"Cidade atual: {aluno_para_atualizar.endereco.cidade}")
        nova_cidade = input("Nova cidade: ")
        if nova_cidade:
            aluno_para_atualizar.endereco.cidade = nova_cidade

        print(f"Estado atual: {aluno_para_atualizar.endereco.estado}")
        novo_estado = input("Novo estado: ")
        if novo_estado:
            aluno_para_atualizar.endereco.estado = novo_estado


        print(f"\nDados do aluno **{aluno_buscar}** atualizados com sucesso!")
        
    else:
        print(f"\nAluno com nome: **{aluno_buscar}** não encontrado.")


def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    mostrar_todos_aluno(lista_alunos)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)
    
    if aluno_para_remover:
        lista_alunos.remove(aluno_para_remover)
        print(f"\nAluno **{aluno_para_remover.nome}** excluído com sucesso!")
    else:
        print(f"\nAluno com o nome **{nome_buscar}** não encontrado.")


while True:
    print("""
=== Gerenciador de Alunos ===
1 - Adicionar
2 - Mostrar todos
3 - Atualizar
4 - Excluir
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
            adicionar_aluno(lista_alunos)
            time.sleep(1)
            os.system("cls || clear")
        case 2:
            mostrar_todos_aluno(lista_alunos)
            time.sleep(4)
        case 3:
            atulizar_aluno(lista_alunos)
            time.sleep(4)
        case 4:
            excluir_aluno(lista_alunos)
            time.sleep(4)
        case 0:
            print("\nSaindo do programa...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(2)
    
    if opcao != 0 and opcao != 1:
        os.system("cls || clear")
        
        
        
        
        #depois revise-  2