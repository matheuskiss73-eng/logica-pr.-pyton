import os
import time 
from dataclasses import dataclass
os.system("cls || clear")

lista_alunos =[]

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
        print(f"Nome: {self.nome} \nData de nascimento: {self.data} \nR.A.: {self.ra}\n Curso: {self.curso} \n Endereço: {self.endereco.logradouro}, {self.endereco.numero} - {self.endereco.cidade} - {self.endereco.estado}")



def lista_esta_vazia (lista_alunos):
    if not lista_alunos:
        print("\nNão há Alunos cadastrados.")
        return True
    return False

def adicionar_aluno (lista_alunos):
    print("\n--- Adicionar novo Aluno ---")
    nome = input("Digite seu nome: ")
    data = input("Digite seu Data de nascimento: ")
    ra = input("Digite seu R.A.: ")
    curso = input("Digite seu Curso: ")
    endereco = Endereco(logradouro = input("Digite o seu logradouro: "), numero = int(input("Digite o número: ")), cidade = input("Digite a cidade: "), estado=input("Digite o estado: "))


    novo_aluno = Aluno(nome=nome, data=data, ra=ra, curso=curso,endereco=endereco)
    lista_alunos.append(novo_aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")


def encontrar_aluno_por_nome(lista_alunos, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for aluno in lista_alunos:
        if nome_buscar_lower.lower() == nome_buscar_lower:
            return aluno
    return None 



def mostrar_todos_aluno (lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    print("\n--- Lista de alunos ---")
    for aluno in lista_alunos:
        print(f"{aluno.mostrar_dados()}")


def atulizar_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return


    mostrar_todos_aluno(lista_alunos)
    print("====== atualizar dados do alunos======")
    aluno_buscar = input("\nDigite o nome do aluno: ")
    aluno_para_atualizar = encontrar_aluno_por_nome(lista_alunos, aluno_buscar)

    if aluno_para_atualizar:
        print("\Aluno não contrado.")
        print("\nDigite os novos dados ou deixe em branco para manter o valor atual")

        print(f"\naluno atual: {aluno_para_atualizar.nome}")
        novo_nome = input("Novo aluno: ")


        print(f"\nData de nascimento atual: {aluno_para_atualizar.data}")
        novo_data = input("Novo Nome: ")

        print(f"\nR.A. atual: {aluno_para_atualizar.ra}")
        novo_ra = input("Novo telefone: ")
        
        print(f"\nCurso atual: {aluno_para_atualizar.curso}")
        novo_curso = input("Novo curso: ")
        
        print(f"\nEndereco atual: {aluno_para_atualizar.endereco}")
        novo_endereco = input("Novo endereco: ")


        if novo_nome:
            aluno_para_atualizar.nome = novo_nome
        if novo_data:
            aluno_para_atualizar.data = novo_data
        if novo_ra:
            aluno_para_atualizar.ra = novo_ra
        if novo_curso:
            aluno_para_atualizar.curso = novo_curso
        if novo_endereco:
            aluno_para_atualizar.endereco = novo_endereco

            print(f"\nDados do aluno: {aluno_buscar} atualizados com sucesso!")
        else:
            print(f"\naluno com nome: {aluno_buscar} não encontrado.")


def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    mostrar_todos_aluno(lista_alunos)

    nome_buscar = input("\nDigite o nome do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_buscar)
    
    if aluno_para_remover:
        lista_alunos.remove(aluno_para_remover)
        print(f"\aluno {aluno_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\aluno com o nome {nome_buscar} não encontrado.")


while True:
    print("""
=== Gerenciador de alunos ===
1 - Adicionar 
2 - Mostrar todos
3 - Atualizar 
4 - Excluir
0 - Sair        
          """)
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada invalida. Digite um numero...")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_aluno(lista_alunos)
        case 3:
            atulizar_aluno(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
        case 0:
            print("\nSaindo do programa cliente...")
            break
        case _:
            print("\nOpção invalida. \n tente novamente.")



    if opcao != 1 and opcao !=0:
        time.sleep(4)
    elif opcao == 1:
        time.sleep(1)

        if opcao!=0:
            os.system("cls || clear")
            
            
            
            #depois revise