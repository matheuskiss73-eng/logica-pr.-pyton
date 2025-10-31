import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    telefone:int
    email: str
    
QUANTIDADE_ALUNOS = 2
lista_alunos = []


print("Solicitando dados do aluno.")
for i in range (QUANTIDADE_ALUNOS):
    print("=======================================")
    aluno = Aluno(
        nome= input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        telefone=int(input("Digite seu telefone: ")),
        email=input("Digite o seu email: ")
       
    )
    lista_alunos.append(aluno)
    
    
print()
print("Salvando dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(
            f"============================\nNome: {aluno.nome}Idade: {aluno.idade}\nTelefone: {aluno.telefone}\nEmail {aluno.email}\n")
    print("Salvo com sucesso.")